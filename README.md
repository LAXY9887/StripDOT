# StripDOT
This is a simple python project to strip "." of Gene Accesssion ID.

## Usage:
    stripDOT [OPTION] [Parameters]
    --input     -i [file path] input file directory
    --targetCol -c [integer number] which coloumn contain transcript ID, default = 3 (bed format)
    --symbol    -s [text] what kind of symbol need to be strip, default = "."
    --outFile   -o [file path/output file.txt] output file directory

## Update 2022-07-15
This tool can also strip other symbols form other column.

### Example:
`stripDOT -i input.bed -c 6 -s "_"`

This will strip "_" from the 6th column in input.bed 
