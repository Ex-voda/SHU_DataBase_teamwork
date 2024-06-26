from flask import jsonify
import psycopg2


class UserManager:
    def __init__(self, db_manager, auth_manager):
        self.db_manager = db_manager
        self.auth_manager = auth_manager

    def verify_credentials(self, cursor, username, password):
        """验证用户凭据并返回用户类型"""
        # 查询管理员表
        query_admin = """SELECT "Ano" FROM "Admin" WHERE "Ano" = %s AND "Akey" = %s"""
        cursor.execute(query_admin, (username, password))
        if cursor.rowcount > 0:
            return "A"

        # 查询教师表
        query_teacher = """SELECT "Tno" FROM "Teacher" WHERE "Tno" = %s AND "Tkey" = %s"""
        cursor.execute(query_teacher, (username, password))
        if cursor.rowcount > 0:
            return "T"

        # 查询学生表
        query_student = """SELECT "Sno" FROM "Student" WHERE "Sno" = %s AND "Skey" = %s"""
        cursor.execute(query_student, (username, password))
        if cursor.rowcount > 0:
            return "S"

        return None

    def get_user_info(self, cursor, user_type, username):
        """根据用户类型获取用户信息"""
        user_type = user_type.strip()
        if user_type == "A":
            return self.__get_admin_info(cursor, username)

        elif user_type == "T":
            return self.__get_teacher_info(cursor, username)

        elif user_type == "S":
            return self.__get_student_info(cursor, username)

        return {}

    def __get_admin_info(self, cursor, username):
        """获取管理员信息"""
        query = """SELECT "Ano", "Akey" FROM "Admin" WHERE "Ano" = %s"""
        cursor.execute(query, (username,))
        row = cursor.fetchone()
        if row:
            return {
                "Uno": row[0],
                "Key": row[1],
                "status": "A",
                "flag": "True"
            }
        return {}

    def __get_teacher_info(self, cursor, username):
        """获取教师信息"""
        query = """SELECT "Tno", "Tkey" FROM "Teacher" WHERE "Tno" = %s"""
        cursor.execute(query, (username,))
        row = cursor.fetchone()
        if row:
            return {
                "Uno": row[0],
                "Key": row[1],
                "status": "T",
                "flag": "True"
            }
        return {}

    def __get_student_info(self, cursor, username):
        """获取学生信息"""
        query = """SELECT "Sno", "Skey" FROM "Student" WHERE "Sno" = %s"""
        cursor.execute(query, (username,))
        row = cursor.fetchone()
        if row:
            return {
                "Uno": row[0],
                "Key": row[1],
                "status": "S",
                "flag": "True"
            }
        return {}
    
    
        
        
        
    # 学分完成情况
    def student_scredit_complete_situation(self, cursor, sno):
        query = """
            SELECT
                "Scredit"."Cno",
                "Course"."Cname",
                "Course"."Credit"
            FROM
                "Scredit"
            JOIN
                "Course" ON "Course"."Cno" = "Scredit"."Cno"
            WHERE
                "Scredit"."Sno" = %(sno)s
        """
        parameters = {'sno': sno}
        cursor.execute(query, parameters)
        rows = cursor.fetchall()
        
        enrolled_courses = [
            {
                "Cno": row[0],
                "Cname": row[1],
                "Credit": row[2],
            }
            for row in rows
        ]

        return enrolled_courses
    
    
    
    
    
    # 课程信息查询
    def get_course(
        self,
        cursor,
        cno="",
        cname="",
        credit="",
        ctno="",
        tname="",
        crtime="",
    ):

        # 添加约束条件
        where_conditions = []
        parameters = {}

        if cno != "":
            where_conditions.append(""""Course"."Cno" = %(Cno_)s""")
            parameters["Cno_"] = cno
        if cname != "":
            where_conditions.append(""""Course"."Cname" = %(Cname_)s""")
            parameters["Cname_"] = cname
        if credit != "":
            where_conditions.append(""""Course"."Credit" = %(Credit_)s""")
            parameters["Credit_"] = credit
        if ctno != "":
            where_conditions.append(""""Course"."Ctno" = %(Ctno_)s""")
            parameters["Ctno_"] = ctno
        if tname != "":
            where_conditions.append(""""Teacher"."Tname" = %(Tname_)s""")
            parameters["Tname_"] = tname
        if crtime != "":
            where_conditions.append(""""ClassRoom"."CRtime" = %(CRtime_)s""")
            parameters["CRtime_"] = crtime

        
        # 构建 SQL 查询分页的语句
        schedule_query = """
            SELECT
                "Course"."Cno",
                "Course"."Cname",
                "Course"."Credit",
                "Course"."Ctno",
                "Teacher"."Tname",
                "ClassRoom"."CRtime"
            FROM
                "Course"
            JOIN
                "Teacher" ON "Teacher"."Tno" = "Course"."Tno"
            JOIN
                "ClassRoom" ON "ClassRoom"."Cno" = "Course"."Cno"
        """
        if where_conditions:
            schedule_query += " WHERE " + " AND ".join(where_conditions)

        # 执行分页查询
        cursor.execute(schedule_query, parameters)
        rows = cursor.fetchall()
        course_exist_ = [
            {
                "Cno": row[0],
                "Cname": row[1],
                "Credit": row[2],
                "Ctno": row[3],
                "Tname": row[4],
                "CRtime": row[5],
            }
            for row in rows
        ]
        # 将结果返回
        return course_exist_
    
    
    
    
    
    # 学生项目查询
    def get_project(self, cursor, sno):
        # 查询项目信息
        proj_query = """
            SELECT
                "Project"."Pno",
                "Project"."Pname",
                "Project"."Sno",
                "Student"."Sname",
                "Project"."Tno",
                "Teacher"."Tname"
            FROM
                "Project"
            JOIN
                "Student" ON "Student"."Sno" = "Project"."Sno"
            JOIN
                "Teacher" ON "Teacher"."Tno" = "Project"."Tno"
            WHERE
                "Project"."Sno" = %(sno)s
        """
        proj_parameters = {'sno': sno}
        cursor.execute(proj_query, proj_parameters)
        rows = cursor.fetchall()
        
        project_info = [
            {
                "Pno": row[0],
                "Pname": row[1],
                "Sno": row[2],
                "Sname": row[3],
                "Tno": row[4],
                "Tname": row[5]
            }
            for row in rows
        ]
        # 查询每个项目的组员信息并添加到项目信息中
        projmen_info = []
        for proj in project_info:
            pno = proj['Pno']
            proj_mem_query = """
                SELECT "ProjMen"."Sno", "Student"."Sname"
                FROM "ProjMen"
                JOIN "Student" ON "ProjMen"."Sno" = "Student"."Sno"
                WHERE "Pno" = %(pno)s
            """
            proj_mem_parameters = {'pno': pno}
            cursor.execute(proj_mem_query, proj_mem_parameters)
            mem_rows = cursor.fetchall()
            per_projmen_info = [
                {"Sno": mem_row[0], "Sname": mem_row[1]}
                for mem_row in mem_rows
            ]
            projmen_info.append(per_projmen_info)

        return project_info, projmen_info

    
    
    
    
    # 学生项目创建
    def insert_project_into_database(
        self, 
        cursor, 
        pname="", 
        psno_leader="", 
        ptno="", 
        psno_members=None
        ):
        try:
            # 生成项目号 pno
            # 获取指导老师的学院号 Cono 
            # cursor.fetchone()[0]执行了数据库查询并提取了结果集中的第一行的第一个值。
            # 在这个上下文中，它是从数据库中获取了指导老师的学院号 Cono。 
            # fetchone() 方法用于检索结果集中的下一行，而 [0] 用于提取该行的第一个列的值。
            cursor.execute(
                """
                SELECT "Cono" FROM "Teacher" WHERE "Teacher"."Tno" = %(ptno)s
                """, 
                {"ptno": ptno}
            )
            cono = cursor.fetchone()[0]

            # 获取当前 Project 表中项目数量
            #在这句代码中，1:04 是一个字符串格式化的操作，它指定了输出的格式。具体来说，{project_count + 1:04} 的含义如下：
            #project_count + 1 是要格式化的值，表示当前项目数量加一。
            #:04 指定了输出的格式。04 表示输出的数字要占据至少四个位置，如果数字不够四位，则用零填充左侧以达到指定的宽度。
            #所以，这段代码的作用是将 project_count + 1 格式化为至少四位的字符串，不足四位的部分用零填充。
            cursor.execute(
                """
                    SELECT COUNT(*) FROM "Project"
                """
            )
            project_count = cursor.fetchone()[0]

            # 构建项目编号 pno
            pno = f"{cono}{psno_leader[6:]}{project_count + 1:04}"

            # 插入数据到 Project 表
            cursor.execute(
                """
                INSERT INTO "Project" ("Pno", "Pname", "Sno", "Tno")
                VALUES (%(pno)s, %(pname)s, %(psno_leader)s, %(ptno)s)
                """,
                {"pno": pno, "pname": pname, "psno_leader": psno_leader, "ptno": ptno},
            )

            # 插入数据到 ProjMen 表
            for psno_member in psno_members:
                cursor.execute(
                    """
                    INSERT INTO "ProjMen" ("Pno", "Sno")
                    VALUES (%(pno)s, %(psno_member)s)
                    """,
                    {"pno": pno, "psno_member": psno_member},
                )

            # 提交事务，事务用来确保一系列的数据库操作要么全部成功执行，要么全部回滚（撤销），以保持数据的一致性和完整性
            cursor.connection.commit()

            # 返回所需的信息
            return {
                "Info": {"Pname": pname, "PSno": psno_members},
                "PTno": ptno,
                "flag": "True"  # 表示操作成功
            }
        except Exception as e:
            # 如果出现异常，回滚事务
            cursor.connection.rollback()

            # 返回失败的信息
            return {
                "Info": {"Pname": pname, "PSno": psno_members},
                "PTno": ptno,
                "flag": "False",  # 表示操作失败
                "message": str(e)  # 返回异常信息
            }

        
    
    
    
    # 学生教室查询
    def get_classroom(
        self,
        cursor,
        crno="",
        crtime="",
        cno="",
        ctno="",
    ):

        # 添加约束条件
        where_conditions = []
        parameters = {}

        if crno != "":
            where_conditions.append(""""ClassRoom"."CRno" = %(CRno_)s""")
            parameters["CRno_"] = crno
        if crtime != "":
            where_conditions.append(""""ClassRoom"."CRtime" = %(CRtime_)s""")
            parameters["CRtime_"] = crtime
        if cno != "":
            where_conditions.append(""""ClassRoom"."Cno" = %(Cno_)s""")
            parameters["Cno_"] = cno
        if ctno != "":
            where_conditions.append(""""ClassRoom"."Ctno" = %(Ctno_)s""")
            parameters["Ctno_"] = ctno

        
        # 构建 SQL 查询分页的语句
        classroom_query = """
            SELECT
                "ClassRoom"."CRno",
                "ClassRoom"."CRtime",
                "ClassRoom"."Cno",
                "ClassRoom"."Ctno",
                "Teacher"."Tname",
                "Course"."Cname"
            FROM
                "ClassRoom"
            JOIN
                "Course" ON "Course"."Cno" = "ClassRoom"."Cno" AND "Course"."Ctno" = "ClassRoom"."Ctno"
            JOIN
                "Teacher" ON "Teacher"."Tno" = "Course"."Tno"
        """
        if where_conditions:
            classroom_query += " WHERE " + " AND ".join(where_conditions)

        cursor.execute(classroom_query, parameters)
        rows = cursor.fetchall()
        classroom_exist_ = [
            {
                "CRno": row[0],
                "CRtime": row[1],
                "Cno": row[2],
                "Ctno": row[3],
                "Tname": row[4],
                "Cname": row[5],
            }
            for row in rows
        ]
        # 将结果返回
        return classroom_exist_
        
        
        
        
    
    # 会议室查询    
    def get_meetingroom_situation(self, cursor, mrno):
        try:
            # 执行查询操作
            cursor.execute(
                """
                SELECT "MRno", "Sno" AS "Uno", "MRtime"
                FROM "MeetingRoomS"
                WHERE (%(mrno)s = '' OR "MRno" = %(mrno)s)
                UNION
                SELECT "MRno", "Tno" AS "Uno", "MRtime"
                FROM "MeetingRoomT"
                WHERE (%(mrno)s = '' OR "MRno" = %(mrno)s)
                UNION
                SELECT "MRno", "Ano" AS "Uno", "MRtime"
                FROM "MeetingRoomA"
                WHERE (%(mrno)s = '' OR "MRno" = %(mrno)s)
                ORDER BY "MRtime"
                """,
                {"mrno": mrno}
            )
            # 获取查询结果
            rows = cursor.fetchall()

            # 初始化一个字典用于合并相同的 MRno
            meetingroom_dict = {}
            for row in rows:
                mrno = row[0]
                uno = row[1]
                mrtime = row[2]
                if mrno not in meetingroom_dict:
                    meetingroom_dict[mrno] = {"Uno": [], "MRtime": []}
                meetingroom_dict[mrno]["Uno"].append(uno)
                meetingroom_dict[mrno]["MRtime"].append(mrtime)

            # 将字典转换为所需的列表格式
            meetingroom_situation = [
                {
                    "MRno": mrno,
                    "Uno": details["Uno"],
                    "MRtime": details["MRtime"]
                }
                for mrno, details in meetingroom_dict.items()
            ]

            # 返回查询结果
            return meetingroom_situation
        except Exception as e:
            # 如果出现异常，返回错误消息
            return {"message": str(e)}

    
    
    
    
    # 会议室预约
    def meetingroom_order(self, cursor, mrno="", mrtime="", uno=""):
        # 插入数据到学生表 MeetingRoomS
        try:
            cursor.execute(
                """
                INSERT INTO "MeetingRoomS" ("MRno", "Sno", "MRtime")
                VALUES (%(mrno)s, %(uno)s, %(mrtime)s)
                """,
                {"mrno": mrno, "uno": uno, "mrtime": mrtime},
            )
            # 提交事务
            cursor.connection.commit()

            # 返回成功信息
            return {
                "flag": "True"
            }
        except Exception as e:
            # 如果出现异常，回滚事务
            cursor.connection.rollback()
            print(mrno, mrtime, uno)
            print(e)
            # 返回错误信息
            return {
                "flag": "False",
                "message": str(e)  # 返回错误信息，便于调试
            }





    # 我的会议室查询
    def get_my_meetingroom_S(self, cursor, uno=""):
        try:
            # 检查是否提供了 Sno
            if uno == "":
                return {"message": "Uno is required."}

            # 查询 MeetingRoomS 表
            query_s = """
                SELECT "MRno", "Sno" AS "Uno", "MRtime"
                FROM "MeetingRoomS"
                WHERE "Sno" = %(uno_)s
            """
            cursor.execute(query_s, {"uno_": uno})
            rows_s = cursor.fetchall()

            # 查询 MeetingRoomT 表
            query_t = """
                SELECT "MRno", "Tno" AS "Uno", "MRtime"
                FROM "MeetingRoomT"
                WHERE "Tno" = %(uno_)s
            """
            cursor.execute(query_t, {"uno_": uno})
            rows_t = cursor.fetchall()

            # 查询 MeetingRoomA 表
            query_a = """
                SELECT "MRno", "Ano" AS "Uno", "MRtime"
                FROM "MeetingRoomA"
                WHERE "Ano" = %(uno_)s
            """
            cursor.execute(query_a, {"uno_": uno})
            rows_a = cursor.fetchall()

            # 合并查询结果
            rows = rows_s + rows_t + rows_a

            meetingroom_dict = {}
            for row in rows:
                mrno = row[0]
                uno = row[1]
                mrtime = row[2]
                if mrno not in meetingroom_dict:
                    meetingroom_dict[mrno] = {"Uno": [], "MRtime": []}
                meetingroom_dict[mrno]["Uno"].append(uno)
                meetingroom_dict[mrno]["MRtime"].append(mrtime)
            meetingroom_res = []
            for mron in meetingroom_dict:
                meetingroom_res.append(
                    {
                        "MRno": mron,
                        "Uno": meetingroom_dict[mron]["Uno"],
                        "MRtime": meetingroom_dict[mron]["MRtime"]
                    }
                )
            # 返回结果
            return meetingroom_res
        except Exception as e:
            # 如果出现异常，返回错误消息
            return {"message": str(e)}



    
        
    #学生会议室预约删除
    def meetingroom_delete_S(self, cursor, mrno="", sno=""):
        # 检查参数是否都有值，如果不是则返回消息
        if not mrno or not sno:
            return {"MRno": mrno, "Sno": sno, "flag": "0", "message": "Both MRno and Sno must be provided for deletion."}

        # 构建 SQL 删除语句
        delete_query = """
            DELETE FROM "MeetingRoomS"
            WHERE "MRno" = %(MRno)s AND "Sno" = %(Sno)s
        """

        # 执行删除操作
        cursor.execute(delete_query, {"MRno": mrno, "Sno": sno})

        # 检查是否成功删除
        if cursor.rowcount > 0:
            # 提交事务
            cursor.connection.commit()
            return "True"
        else:
            # 如果出现异常，回滚事务
            cursor.connection.rollback()
            return "False"
        
        
        
        

    # 教师方法
    # 教分完成情况
    def teacher_tcredit_complete_situation(self, cursor, tno):
        query = """
            SELECT
                "Tcredit"."Tno",
                "Course"."Cname",
                "Course"."Credit"
            FROM
                "Tcredit"
            JOIN
                "Course" ON "Course"."Cno" = "Tcredit"."Cno"
            WHERE
                "Tcredit"."Tno" = %(tno)s
        """
        parameters = {'tno': tno}
        cursor.execute(query, parameters)
        rows = cursor.fetchall()
        
        teached_courses = [
            {
                "Cno": row[0],
                "Cname": row[1],
                "Credit": row[2],
            }
            for row in rows
        ]

        return teached_courses





    # 教师项目查询
    def get_project_T(self, cursor, tno):
        # 查询项目信息
        proj_query = """
            SELECT
                "Project"."Pno",
                "Project"."Pname",
                "Project"."Sno",
                "Student"."Sname",
                "Project"."Tno",
                "Teacher"."Tname"
            FROM
                "Project"
            JOIN
                "Student" ON "Student"."Sno" = "Project"."Sno"
            JOIN
                "Teacher" ON "Teacher"."Tno" = "Project"."Tno"
            WHERE
                "Project"."Tno" = %(tno)s
        """
        proj_parameters = {'tno': tno}
        cursor.execute(proj_query, proj_parameters)
        rows = cursor.fetchall()
        
        project_info = [
            {
                "Pno": row[0],
                "Pname": row[1],
                "Sno": row[2],
                "Sname": row[3],
                "Tno": row[4],
                "Tname": row[5]
            }
            for row in rows
        ]
        # 查询每个项目的组员信息并添加到项目信息中
        projmen_info = []
        for proj in project_info:
            pno = proj['Pno']
            proj_mem_query = """
                SELECT "ProjMen"."Sno", "Student"."Sname"
                FROM "ProjMen"
                JOIN "Student" ON "ProjMen"."Sno" = "Student"."Sno"
                WHERE "Pno" = %(pno)s
            """
            proj_mem_parameters = {'pno': pno}
            cursor.execute(proj_mem_query, proj_mem_parameters)
            mem_rows = cursor.fetchall()
            per_projmen_info = [
                {"Sno": mem_row[0], "Sname": mem_row[1]}
                for mem_row in mem_rows
            ]
            projmen_info.append(per_projmen_info)

        return project_info, projmen_info





    # 会议室预约
    def meetingroom_order_T(self, cursor, mrno="", mrtime="", uno=""):
        # 插入数据到学生表 MeetingRoomS
        try:
            cursor.execute(
                """
                INSERT INTO "MeetingRoomT" ("MRno", "Tno", "MRtime")
                VALUES (%(mrno)s, %(uno)s, %(mrtime)s)
                """,
                {"mrno": mrno, "uno": uno, "mrtime": mrtime},
            )
            # 提交事务
            cursor.connection.commit()

            # 返回成功信息
            return {
                "flag": "True"
            }
        except Exception as e:
            # 如果出现异常，回滚事务
            cursor.connection.rollback()
            print(mrno, mrtime, uno)
            print(e)
            # 返回错误信息
            return {
                "flag": "False",
                "message": str(e)  # 返回错误信息，便于调试
            }
            
            
            
            
           
    #会议室预约删除
    def meetingroom_delete_T(self, cursor, mrno="", tno=""):
        # 检查参数是否都有值，如果不是则返回消息
        if not mrno or not tno:
            return {"MRno": mrno, "Tno": tno, "flag": "0", "message": "Both MRno and Tno must be provided for deletion."}

        # 构建 SQL 删除语句
        delete_query = """
            DELETE FROM "MeetingRoomT"
            WHERE "MRno" = %(MRno)s AND "Tno" = %(Tno)s
        """

        # 执行删除操作
        cursor.execute(delete_query, {"MRno": mrno, "Tno": tno})

        # 检查是否成功删除
        if cursor.rowcount > 0:
            # 提交事务
            cursor.connection.commit()
            return "True"
        else:
            # 如果出现异常，回滚事务
            cursor.connection.rollback()
            return "False"
        
        
        
        
         
    # 管理员方法
    # 学生信息查询
    def get_student(
        self,
        cursor,
        sno="",
        sname="",
        grade="",
        sgender="",
        cono="",
        cname="",
    ):

        # 添加约束条件
        where_conditions = []
        parameters = {}

        if sno != "":
            where_conditions.append(""""Student"."Sno" = %(Sno_)s""")
            parameters["Sno_"] = sno
        if sname != "":
            where_conditions.append(""""Student"."Sname" = %(Sname_)s""")
            parameters["Sname_"] = sname
        if grade != "":
            where_conditions.append(""""Student"."Grade" = %(Grade_)s""")
            parameters["Grade_"] = grade
        if sgender != "":
            where_conditions.append(""""Student"."Sgender" = %(Sgender_)s""")
            parameters["Sgender_"] = sgender
        if cono != "":
            where_conditions.append(""""Student"."Cono" = %(Cono_)s""")
            parameters["Cono_"] = cono
        if cname != "":
            where_conditions.append(""""College"."Cname" = %(Cname_)s""")
            parameters["Cname_"] = cname

        
        # 构建 SQL 查询分页的语句
        schedule_query = """
            SELECT
                "Student"."Sno",
                "Student"."Sname",
                "Student"."Grade",
                "Student"."Sgender",
                "College"."Cname"
            FROM
                "Student"
            JOIN
                "College" ON "College"."Cono" = "Student"."Cono"
        """
        if where_conditions:
            schedule_query += " WHERE " + " AND ".join(where_conditions)

        # 执行分页查询
        cursor.execute(schedule_query, parameters)
        rows = cursor.fetchall()
        student_exist_ = [
            {
                "Sno": row[0],
                "Sname": row[1],
                "Grade": row[2],
                "Sgender": row[3],
                "Cname": row[4],
            }
            for row in rows
        ]
        # 将结果返回
        return student_exist_
    
    
    
    
    
    # 教师信息查询
    def get_teacher(
        self,
        cursor,
        tno="",
        tname="",
        tlevel="",
        tgender="",
        cono="",
        cname="",
    ):

        # 添加约束条件
        where_conditions = []
        parameters = {}

        if tno != "":
            where_conditions.append(""""Teacher"."Tno" = %(Tno_)s""")
            parameters["Tno_"] = tno
        if tname != "":
            where_conditions.append(""""Teacher"."Tname" = %(Tname_)s""")
            parameters["Tname_"] = tname
        if tlevel != "":
            where_conditions.append(""""Teacher"."Tlevel" = %(Tlevel_)s""")
            parameters["Tlevel_"] = tlevel
        if tgender != "":
            where_conditions.append(""""Teacher"."Tgender" = %(Tgender_)s""")
            parameters["Tgender_"] = tgender
        if cono != "":
            where_conditions.append(""""Teacher"."Cono" = %(Cono_)s""")
            parameters["Cono_"] = cono
        if cname != "":
            where_conditions.append(""""College"."Cname" = %(Cname_)s""")
            parameters["Cname_"] = cname

        
        # 构建 SQL 查询分页的语句
        schedule_query = """
            SELECT
                "Teacher"."Tno",
                "Teacher"."Tname",
                "Teacher"."Tlevel",
                "Teacher"."Tgender",
                "College"."Cname"
            FROM
                "Teacher"
            JOIN
                "College" ON "College"."Cono" = "Teacher"."Cono"
        """
        if where_conditions:
            schedule_query += " WHERE " + " AND ".join(where_conditions)

        # 执行分页查询
        cursor.execute(schedule_query, parameters)
        rows = cursor.fetchall()
        teacher_exist_ = [
            {
                "Tno": row[0],
                "Tname": row[1],
                "Tlevel": row[2],
                "Tgender": row[3],
                "Cname": row[4],
            }
            for row in rows
        ]
        # 将结果返回
        return teacher_exist_
    
    
    
    
    
    # 会议室预约
    def meetingroom_order_A(self, cursor, mrno="", mrtime="", uno=""):
        # 插入数据到学生表 MeetingRoomS
        try:
            cursor.execute(
                """
                INSERT INTO "MeetingRoomA" ("MRno", "Ano", "MRtime")
                VALUES (%(mrno)s, %(uno)s, %(mrtime)s)
                """,
                {"mrno": mrno, "uno": uno, "mrtime": mrtime},
            )
            # 提交事务
            cursor.connection.commit()

            # 返回成功信息
            return {
                "flag": "True"
            }
        except Exception as e:
            # 如果出现异常，回滚事务
            cursor.connection.rollback()
            print(mrno, mrtime, uno)
            print(e)
            # 返回错误信息
            return {
                "flag": "False",
                "message": str(e)  # 返回错误信息，便于调试
            }
            
            
            
            
            
    #会议室预约删除
    def meetingroom_delete_A(self, cursor, mrno="", ano=""):
        # 检查参数是否都有值，如果不是则返回消息
        if not mrno or not ano:
            return {"MRno": mrno, "Ano": ano, "flag": "0", "message": "Both MRno and Ano must be provided for deletion."}

        # 构建 SQL 删除语句
        delete_query = """
            DELETE FROM "MeetingRoomA"
            WHERE "MRno" = %(MRno)s AND "Ano" = %(Ano)s
        """

        # 执行删除操作
        cursor.execute(delete_query, {"MRno": mrno, "Ano": ano})

        # 检查是否成功删除
        if cursor.rowcount > 0:
            # 提交事务
            cursor.connection.commit()
            return "True"
        else:
            # 如果出现异常，回滚事务
            cursor.connection.rollback()
            return "False"