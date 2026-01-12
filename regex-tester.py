#!/usr/bin/env python3

import re
import argparse

def parse_args():
	parser = argparse.ArgumentParser()

	parser.add_argument("--engine")
	parser.add_argument("--regex")
	parser.add_argument("--string")

	return parser.parse_args()

def re_explainer(regex):
	explanations = {
		"^": "Start of string",
		"$": "End of string",
		".": "Any single character",
		".*": "Matches any character, between zero and unlimited times",
		"\\d": "Any digit",
		"\\D": "Any non-digit",
		"+": "One or more of preceding character",
		"*": "Zero or more of preceding character",
		"?": "Zero or one of preceding character ie optional",
		"\\b": "Word boundary",
		"\\B": "Non-word boundary",
		"[a-z]": "A character in the range a-z",
	}
	breakdown = []
	for token, definition in explanations.items():
		if token in regex:
			breakdown.append(f"{token: {definition}")

		if breakdown:
			return breakdown
		else:
			print(f"No tokens detected")

def main():
	args = parse_args()

	try:
		pattern = re.compile(args.regex)
	except re.error as error:
		print(f"Invalid regex: {error}")
		return
