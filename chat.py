lines = []
# 輸入檔案
def read_file(filename):
	with open(filename, "r", encoding = "UTF-8-sig") as f:
		for line in f:
			a = line.strip()
			lines.append(a)
	return lines


#添加名字
def convert(lines):
	new = []
	# 先宣告name這個變數
	name = None #宣告name這個變數是none;其他語言是Null
	for line in lines:
		if line == "Allen":
			name = "Allen"
			continue # continue以後的程式碼都會跳過
		elif line == "Tom":
			name = "Tom"
			continue # continue以後的程式碼都會跳過
		if name: #if person 有值的話
			new.append(name + ": " + line)
	return new

#寫入檔案
def write_file(filename, lines):
	with open(filename,"w") as f:
		for line in lines:
			f.write(line + "\n")




def main():	 #進入程式的執行碼
	lines = read_file("input.txt") #將檔名變成參數，使用時才決定要使用某特定的檔案
	lines = convert(lines)
	write_file("output.txt", lines)

	

main() #進入點
