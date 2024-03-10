##~---------------------------------------------------------------------------##
##                               *       +                                    ##
##                         '                  |                               ##
##                     ()    .-.,="``"=.    - o -                             ##
##                           '=/_       \     |                               ##
##                        *   |  '=._    |                                    ##
##                             \     `=./`,        '                          ##
##                          .   '=.__.=' `='      *                           ##
##                 +                         +                                ##
##                      O      *        '       .                             ##
##                                                                            ##
##  File      : build-game.ps1                                                ##
##  Project   : Ram it                                                        ##
##  Date      : 2024-03-10                                                    ##
##  License   : See project's COPYING.TXT for full info.                      ##
##  Author    : mateus.digital <hello@mateus.digital>                         ##
##  Copyright : mateus.digital - 2024                                         ##
##                                                                            ##
##  Description :                                                             ##
##     Builds the game to windows platform.                                   ##
##     Requires pyinstaller to be present - if not open a adm pwsh and run:   ##
##       pip install -U pyinstaller                                           ##
##---------------------------------------------------------------------------~##

$OUTPUT_FOLDER = "build-pc-Release";
$EXE_NAME      = "ram-it";

## Clean output...
if(Test-Path "$OUTPUT_FOLDER") {
    Remove-Item -Path "$OUTPUT_FOLDER" -Force -Recurse;
}

New-Item -ItemType Directory -Path "$OUTPUT_FOLDER";

# Build the game.
pyinstaller.exe .\src\main.py      `
    -i .\assets\ramit_icon.ico     `
    -n            "$EXE_NAME"      `
    --distpath    "$OUTPUT_FOLDER" `
    --noconsole                    `
    ;

## Copy Assets to the build folder
Copy-Item -Recurse ./assets "$OUTPUT_FOLDER/$EXE_NAME";

## Clean up.
Remove-Item (Get-ChildItem -Path . -Filter *.spec -Recurse -ErrorAction SilentlyContinue -Force)