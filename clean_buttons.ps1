$utf8NoBom = New-Object System.Text.UTF8Encoding $false
$files = (Get-ChildItem "*.html","*.htm" -File) + (Get-ChildItem "projects\*.html" -File)

foreach ($f in $files) {
  $c = [System.IO.File]::ReadAllText($f.FullName, [System.Text.Encoding]::UTF8)
  $orig = $c.Length

  # Remove navbar-cart block (Webflow ecommerce cart widget)
  $c = [regex]::Replace($c, '(?s)<div class="navbar-cart">.*?</div>\s*', '')

  # Remove orphan <div>...</div> wrapper left after purchase-wrap removal
  $c = [regex]::Replace($c, '(?s)<div>\s*</a></div>', '')

  # Remove any leftover purchase-wrap divs
  $c = [regex]::Replace($c, '(?s)<div class="purchase-wrap">.*?</div>', '')

  # Remove ALL PAGES button (w-variant-7de8b098)
  $c = [regex]::Replace($c, '(?s)<a[^>]*w-variant-7de8b098-3e90-ba8b-bd0d-4ac008101edb[^>]*>.*?</a>', '')

  [System.IO.File]::WriteAllText($f.FullName, $c, $utf8NoBom)
  $removed = $orig - $c.Length
  if ($removed -gt 0) { Write-Host "Cleaned $($f.Name): -$removed chars" }
}
Write-Host "All done"
