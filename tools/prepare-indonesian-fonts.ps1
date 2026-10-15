param(
    [Parameter(Mandatory = $true)]
    [string] $GameRoot,

    [string] $OutputDirectory = (Join-Path $PSScriptRoot '..\dist\indonesian-support')
)

$ErrorActionPreference = 'Stop'

$fontFiles = @(
    @{
        RelativePath = 'language\fonts\Small.bin'
        SizeBytes = 40448
        Sha256 = 'F194F96F9389BA7F4CB126AC02E2F619F27DF0339AB97DF6FE7A740E5A1FCA35'
    },
    @{
        RelativePath = 'language\fonts\Big.bin'
        SizeBytes = 72832
        Sha256 = '119EDE7EC211DDEBDE76B46E4DCBEA86E486F1B13549FC1FE58ECB5ED59611C5'
    }
)

$gameRootPath = [System.IO.Path]::GetFullPath($GameRoot)
if ([System.IO.Path]::IsPathRooted($OutputDirectory)) {
    $outputRootPath = [System.IO.Path]::GetFullPath($OutputDirectory)
}
else {
    $outputRootPath = [System.IO.Path]::GetFullPath((Join-Path $PSScriptRoot $OutputDirectory))
}

if (-not (Test-Path -LiteralPath $gameRootPath -PathType Container)) {
    throw "Game root does not exist: $gameRootPath"
}

foreach ($font in $fontFiles) {
    $sourcePath = Join-Path $gameRootPath $font.RelativePath
    if (-not (Test-Path -LiteralPath $sourcePath -PathType Leaf)) {
        throw "Required font file is missing: $sourcePath"
    }

    $sourceItem = Get-Item -LiteralPath $sourcePath
    if ($sourceItem.Length -ne $font.SizeBytes) {
        throw "Unexpected size for $sourcePath. Expected $($font.SizeBytes) bytes; found $($sourceItem.Length)."
    }

    $sourceHash = (Get-FileHash -LiteralPath $sourcePath -Algorithm SHA256).Hash
    if ($sourceHash -ne $font.Sha256) {
        throw "Unexpected SHA-256 for $sourcePath. The source is not the verified BLACK font asset."
    }
}

foreach ($font in $fontFiles) {
    $sourcePath = Join-Path $gameRootPath $font.RelativePath
    $targetPath = Join-Path $outputRootPath $font.RelativePath
    $targetDirectory = Split-Path -Parent $targetPath
    New-Item -ItemType Directory -Path $targetDirectory -Force | Out-Null

    if (Test-Path -LiteralPath $targetPath -PathType Leaf) {
        $existingHash = (Get-FileHash -LiteralPath $targetPath -Algorithm SHA256).Hash
        if ($existingHash -ne $font.Sha256) {
            throw "Refusing to overwrite a different file: $targetPath"
        }
    }
    else {
        Copy-Item -LiteralPath $sourcePath -Destination $targetPath
    }

    Write-Output ("Prepared {0} ({1} bytes, SHA-256 {2})" -f $font.RelativePath, $font.SizeBytes, $font.Sha256)
}

Write-Output "Package ready at: $outputRootPath"
Write-Output 'Copy the language folder into the root of your game installation.'
