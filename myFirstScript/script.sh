rm -rf bigdirectory
mkdir big-directory
cd big-directory
mkdir small-directory
cd small-directory
touch file-1.txt
echo "Brian Tran" > file-1.txt
cat file-1.txt
seq 1 20 > file-1.txt
cat file-1.txt
wc -w file-1.txt
wc -w < file-1.txt >> file-2.txt
cat file-1.txt
cat file2.txt
cp file-1.txt ../file-1.txt
mv file-1.txt file-3.txt
cd ..
rm -rf small-directory
ls -l # -l displays detailed information about directories and files
ls -a # -a shows all files and directories, including hidden ones
cd ..
rm -rf big-directory