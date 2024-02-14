#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def parse(filename: str) -> None:
    with open(filename, 'r', encoding='utf-8-sig') as file:
        return set((line.rstrip() for line in file))

def convert_tokens_to_mysql_queries(table_name: str, column_name: str, tokens: set = set[str]) -> set[str]:
    queries = set()

    for token in tokens:
        query = 'INSERT INTO {0} ({1}) VALUES ("{2}");'.format(table_name, column_name, token)
        queries.add(query)

    return queries
    
def write_to_file(file: str, queries: set[str]) -> None:
        with open(file, 'w') as file:
            file.write('\n'.join(queries))

def main(input_file: str, output_file: str, table_name: str, column_name: str) -> None:
    tokens = parse(filename=input_file)
    
    queries = convert_tokens_to_mysql_queries(table_name=table_name, column_name=column_name, tokens=tokens)

    write_to_file(file=output_file, queries=queries)

if __name__ == "__main__":
    main(
         'your-input.txt', 
         'your-output.txt', 
         'your-tablename', 
         'your-columnname'
    )
