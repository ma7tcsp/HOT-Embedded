#Banner Stuff
function Write-HostColored2(){[CmdletBinding()]param([parameter(Position=0, ValueFromPipeline=$true)] [string[]] $t,[switch] $x,[ConsoleColor] $bc = $host.UI.RawUI.BackgroundColor,[ConsoleColor] $fc = $host.UI.RawUI.ForegroundColor);begin{if ($t -ne $null){$t = "$t"}};process {if ($t) {$cfc = $fc;$cbc = $bc;$ks = $t.split("#");$p = $false;foreach($k in $ks) {if (-not $p -and $k -match '^([a-z]*)(:([a-z]+))?$') {try {$cfc = [ConsoleColor] $matches[1];$p = $true} catch {}if ($matches[3]) {try {$cbc = [ConsoleColor] $matches[3];$p = $true} catch {}}if ($p) {continue}};$p = $false;if ($k) {$argsHash = @{};if ([int] $cfc -ne -1) { $argsHash += @{ 'ForegroundColor' = $cfc } };if ([int] $cbc -ne -1) { $argsHash += @{ 'BackgroundColor' = $cbc } };Write-Host -NoNewline @argsHash $k} $cfc = $fc;$cbc = $bc}} if (-not $x) { write-host }}}
write-host("")
write-host("")
write-host("")
write-host("")
write-host("")
write-host("")
write-host("")
$banner = ("             #darkcyan#▄▄#             
       #yellow#▄▄#  #darkcyan#▄▄██▄▄#  #darkcyan#▄▄#       
       #yellow#██#  #darkcyan#▀▀██▀▀#  #darkcyan#██#       
    #yellow#████████# #darkcyan#▀▀# #darkcyan#████████#    
       #yellow#██#    #red#██#    #darkcyan#██#       ████████╗ █████╗ ██████╗ ██╗     ███████╗ █████╗ ██╗   ██╗
    #darkcyan#██# #yellow#▀▀#    #red#██#    #darkcyan#▀▀# #magenta#██#    ╚══██╔══╝██╔══██╗██╔══██╗██║     ██╔════╝██╔══██╗██║   ██║
  #darkcyan#██████# #red#██████████# #magenta#██████#     ██║   ███████║██████╔╝██║     █████╗  ███████║██║   ██║
    #darkcyan#██# #darkred#▄▄#    #red#██#    #blue#▄▄# #magenta#██#       ██║   ██╔══██║██╔══██╗██║     ██╔══╝  ██╔══██║██║   ██║
       #darkred#██#    #red#██#    #blue#██#          ██║   ██║  ██║██████╔╝███████╗███████╗██║  ██║╚██████╔╝
    #darkred#████████# #magenta#▄▄# #blue#████████#       ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ 
       #darkred#██#  #magenta#▄▄██▄▄#  #blue#██#                  HANDS ON TRAINING INITALIZATION...
       #darkred#▀▀#  #magenta#▀▀██▀▀#  #blue#▀▀#       
             #magenta#▀▀#              ")

Write-HostColored2 $banner
#Tableu Initaliser
write-host("")
write-host("          ======================================================================")
write-host("          Welcome to TC23 Hands On Training - Build An Analytical App           ")
write-host("          Please wait while your environment configures                         ")
write-host("          This will only take a few moments                                     ")
write-host("          When complete, the web portal will launch                             ")
write-host("          Sit back and make yourself conformatble!                              ")
write-host("          ======================================================================")
write-host("")




#Download zip from GitHub
Invoke-WebRequest -Uri "https://github.com/API-Guild/TC23-embed-portal/archive/refs/heads/main.zip" -OutFile "C:\Users\Administrator\Documents\main.zip"
#Unzip 
Expand-Archive "C:\Users\Administrator\Documents\main.zip" -DestinationPath "C:\Users\Administrator\Documents\HOT20" -Force
#Add shortcuts to Desktop\Web
copy-item "C:\Users\Administrator\Documents\VS Code.lnk" -Destination "C:\Users\Administrator\Desktop\VS Code.lnk"
copy-item "C:\Users\Administrator\Documents\Web Portal.lnk" -Destination "C:\Users\Administrator\Desktop\Web Portal.lnk"
Copy-Item "C:\Users\Administrator\Documents\HOT20\TC23-embed-portal-main\Tableau Cloud Site.lnk" -Destination "C:\Users\Administrator\Desktop\Tableau Cloud Site.lnk"
#Edit EmbedPython.py to the specific labUser
#$tabUser = [System.Environment]::GetEnvironmentVariable('labUser')
#write-host $tabUser
$tabUser = get-content 'c:\Users\Administrator\labUser.txt'
#write-host $tabUser
Start-Sleep -Seconds 5
((Get-Content -path C:\Users\Administrator\Documents\HOT20\TC23-embed-portal-main\EmbedPortal.py -Raw) -replace 'user_default',$tabUser) | Set-Content -Path C:\Users\Administrator\Documents\HOT20\TC23-embed-portal-main\EmbedPortal.py
#Launch VS Code and open the course folder
Start powershell {"C:\Users\Administrator\launchvscode.ps1"}
Start-Sleep -Seconds 5
Invoke-Item "C:\Users\Administrator\Desktop\Web Portal.lnk"
