def replace_words(input_file, output_file):
    count = 0
    with open(input_file, 'r') as file:
        text = file.read()
        count = text.count("terrible")
        text = text.replace("terrible", "pathetic", count % 2)  # 偶数次替换
        text = text.replace("terrible", "marvellous", count - (count % 2))  # 奇数次替换
    with open(output_file, 'w') as file:
        file.write(text)
    return count
input_file = "file_to_read.txt"
output_file = "result.txt"
total_count = replace_words(input_file, output_file)
print("Total number of times the word 'terrible' appears:", total_count)
print("The replaced text is saved to the result.txt file.")