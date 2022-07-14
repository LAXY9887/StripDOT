# StripDOT
This is a simple python project to strip "." of Gene Accesssion ID.

## Usage:
    stripDOT [OPTION] [Parameters]
    --input     -i [file path] input file directory
    --targetCol -c [integer number] which coloumn contain transcript ID, default = 3 (bed format)
    --symbol    -s [text] what kind of symbol need to be strip, default = "."
    --outFile   -o [file path/output file.txt] output file directory

## Example1:
`stripDOT -i input.bed`

This will output "converted.txt" at current directory.

## Example2:
`stripDOT -i input.bed -o path/output.txt`

This will output "output.txt" at "path".

## Update 2022-07-15
This tool can also strip other symbols form other column.

### Example:
`stripDOT -i input.bed -c 6 -s "_"`

This will strip "_" from the 6th column in input.bed 

## Download this tool:
`git colne https://github.com/LAXY9887/StripDOT.git`

### or 
Download as zip file and unzip the archive.

Executable file (StripDOT.exe) in /bin
