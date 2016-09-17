from subprocess import call


for i in range(1,255):
  call(["scp", "student@10.11.5.1:/home/student/sys.log student@10.11.5.{}"]).format(i)

