  #读取锁
  with open(latest_time_file) as f_in:
        fcntl.flock(f_in.fileno(), fcntl.LOCK_EX)  # 加锁，with块外自动释放锁
        sql_data = f_in.read()
        fcntl.flock(f_in, fcntl.LOCK_UN)
        
        
        
    #写入锁    
    with open('sql_daily_cmd.csv', 'a+', encoding='utf-8') as f:
        fcntl.flock(f.fileno(), fcntl.LOCK_EX)  # 加锁，with块外自动释放锁
        f.truncate(0)
        cmd_SQL2 = ''' "SELECT A.製造NO AS ロットNo, A.品目KEY, A.品目CD, B.子品目KEY, B.子品目CD, A.指示数 AS 数量, B.実払出数 AS 所要数,  1 AS 前加工有無 FROM D_HR払出計画データ AS A INNER JOIN D_HR払出構成データ AS B ON A.製造NO = B.製造NO WHERE ((A.払出完了日付 = ''' +sql_data_day1 +''' AND A.払出完了時間 > ''' +sql_data_hour1+''' ) or (A.払出完了日付 >= '''+ str(int(sql_data_day1)+1)+''')) AND A.払出完了日付 <> 20991231 AND A.品目CD LIKE '%$' AND A.指示数 <> 0 ORDER BY A.払出完了日付 DESC, A.払出完了時間 DESC  " -o sql_daily_cmd.csv -h-1 -W -s ";" '''
        print('cmd_SQL2',cmd_SQL2)
        cmd2=sql_server+cmd_SQL2
        # print('cmd2',cmd2)
        result = os.popen(cmd2) #run the command
        fcntl.flock(f, fcntl.LOCK_UN)
