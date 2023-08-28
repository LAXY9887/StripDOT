# StripDOT
This is a simple python project to strip "." (or other symbol) of Gene/Transcript IDs form the 4th column of a BED file and export a gene list (text file).

## Usage:
    stripDOT [OPTION] [Parameters]
    --input     -i [file_path/file.bed] input a BED format file.
    --targetCol -c [integer number] which coloumn contain transcript ID, default = 4 (bed format)
    --symbol    -s [string] what kind of symbol need to be strip, default = "."
    --sep       -p [string] Enter input file separation symbol, default = "\\t" (TAB)
    --outFile   -o [file_path/output_file.txt] output a text file.

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

## Update 2022-08-28
This tool can also handle CSV (comma separate) format, it can also specify other symbol.

### Example:
`stripDOT -i input.csv -p "," -o path/output.txt`

The `-p ","` option works on CSV format, and it will output "output.txt" at "path".

## Download this tool:
`git colne https://github.com/LAXY9887/StripDOT.git`

or 
Download as zip file and unzip the archive.

Executable file (StripDOT.exe) in /bin

Execute StripDOT.exe

`StripDOT.exe -i input.bed`

Execute by Python3

`python main.py -i input.bed`
