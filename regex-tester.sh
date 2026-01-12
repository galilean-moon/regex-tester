usage () {
	printf "\nUsage: $(basename "$0") [OPTIONS] [REGEX] [TEST STRING]\n"
	printf "This program accepts a regex string and a test string as inputs, and displays matches with a breakdown of match grouping. Like a bad regex101.\n"
	printf "\nOPTIONS:\n	-h, --help		Show this message\n	-e posix | pcre		Select engine.\n"
	printf "\nREGEX:\n	-regex		The regex to test against the string\n"
	printf "\nTEST STRING:\n	-string		The test string\n"
exit
}

if [[ "$2" = "posix" || "$2" = "pcre" ]]; then
	ENGINE="$1"
	read -p "Enter the regex string: " REGEX
	read -p "Enter the test string: " STRING
else
	usage
fi

[[ -z "$ENGINE" || -z "$REGEX" || -z "STRING" || "$1" = "-h" || "$1" = "--help" ]] && usage

export PYTHONNUMBERBUFFERED=1

python3 regex_python.py \
--engine "$ENGINE" \
--regex "$REGEX" \
--string "$STRING"
