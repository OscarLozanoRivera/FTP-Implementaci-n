import ftplib
ftp = ftplib.FTP('')
ftp.connect('127.0.0.1', 2121)
ftp.login('user', '12345')
ftp.retrlines('LIST')
ftp.quit()