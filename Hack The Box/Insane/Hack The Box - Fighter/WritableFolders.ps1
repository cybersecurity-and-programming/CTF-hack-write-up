function Get-WritableFolders {
    param (
        [string]$path = "C:\"
    )

    $folders = Get-ChildItem -Path $path -Recurse -Directory

    foreach ($folder in $folders) {
        try {
            $acl = Get-Acl $folder.FullName
            $accessRules = $acl.Access | Where-Object { $_.FileSystemRights -match "Write" -and $_.AccessControlType -eq "Allow" }
            if ($accessRules) {
                Write-Output $folder.FullName
            }
        } catch {
            Write-Output "No se pudo acceder a $($folder.FullName)"
        }
    }
}