  #读取锁
  with open(latest_time_file) as f_in:
        fcntl.flock(f_in.fileno(), fcntl.LOCK_EX)  # 加锁，with块外自动释放锁
        sql_data = f_in.read()
        fcntl.flock(f_in, fcntl.LOCK_UN)
        
        
        
    #写入锁    
    with open('sql_daily_cmd.csv', 'a+', encoding='utf-8') as f:
        fcntl.flock(f.fileno(), fcntl.LOCK_EX)  # 加锁，with块外自动释放锁
        f.truncate(0)
        cmd_SQL2 = ''' "select number from table1" -o sql_daily_cmd.csv -h-1 -W -s ";" '''
        print('cmd_SQL2',cmd_SQL2)
        cmd2=sql_server+cmd_SQL2
        # print('cmd2',cmd2)
        result = os.popen(cmd2) #run the command
        fcntl.flock(f, fcntl.LOCK_UN)
