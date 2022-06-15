语句 
SELECT locus,GROUP_CONCAT(id) 
FROM info WHERE locus IN('AB086827','AF040764') GROUP BY locus;的返回结果为
+----------+------------------+
| locus    | GROUP_CONCAT(id) |
+----------+------------------+
| AB086827 | 1,2              |
| AF040764 | 23,24            |
+----------+------------------+

语句 
SELECT locus,GROUP_CONCAT(distinct id ORDER BY id DESC SEPARATOR '_') 
FROM info WHERE locus IN('AB086827','AF040764') GROUP BY locus;的返回结果为
+----------+----------------------------------------------------------+
| locus    | GROUP_CONCAT(distinct id ORDER BY id DESC SEPARATOR '_') |
+----------+----------------------------------------------------------+
| AB086827 | 2_1                                                      |
| AF040764 | 24_23                                                    |
+----------+----------------------------------------------------------+

语句
SELECT locus,GROUP_CONCAT(concat_ws(', ',id,journal) ORDER BY id DESC SEPARATOR '. ') 
FROM info WHERE locus IN('AB086827','AF040764') GROUP BY locus;的返回结果为
+----------+--------------------------------------------------------------------------+
| locus    | GROUP_CONCAT(concat_ws(', ',id,journal) ORDER BY id DESC SEPARATOR '. ') |
+----------+--------------------------------------------------------------------------+
| AB086827 | 2, Submitted (20-JUN-2002). 1, Unpublished                               |
| AF040764 | 24, Submitted (31-DEC-1997) . 23, Unpublished                            |
+----------+--------------------------------------------------------------------------+
