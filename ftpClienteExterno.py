import ftplib
ftp = ftplib.FTP('ftp.dlptest.com')
ftp.login('dlpuser', 'rNrKYTX9g7z3RgJRmxWuGHbeu')
ftp.retrlines('LIST')
ftp.quit()