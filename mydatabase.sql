PGDMP      6    
    
        |         
   mydatabase    16.2    16.2 I    H           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            I           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            J           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            K           1262    16398 
   mydatabase    DATABASE     �   CREATE DATABASE mydatabase WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Chinese (Simplified)_China.936';
    DROP DATABASE mydatabase;
                postgres    false                        2615    2200    public    SCHEMA        CREATE SCHEMA public;
    DROP SCHEMA public;
                pg_database_owner    false            L           0    0    SCHEMA public    COMMENT     6   COMMENT ON SCHEMA public IS 'standard public schema';
                   pg_database_owner    false    4            �            1259    16427    Admin    TABLE     g   CREATE TABLE public."Admin" (
    "Ano" character varying(8) NOT NULL,
    "Akey" character varying
);
    DROP TABLE public."Admin";
       public         heap    postgres    false    4            M           0    0    TABLE "Admin"    COMMENT     6   COMMENT ON TABLE public."Admin" IS '管理员信息';
          public          postgres    false    218            �            1259    16530 	   ClassRoom    TABLE     �   CREATE TABLE public."ClassRoom" (
    "CRno" character varying(4) NOT NULL,
    "Cno" character varying(8),
    "Ctno" character varying(4),
    "CRtime" character varying(4) NOT NULL
);
    DROP TABLE public."ClassRoom";
       public         heap    postgres    false    4            N           0    0    TABLE "ClassRoom"    COMMENT     =   COMMENT ON TABLE public."ClassRoom" IS '教室安排信息';
          public          postgres    false    226            �            1259    16422    College    TABLE     y   CREATE TABLE public."College" (
    "Cono" character varying(2) NOT NULL,
    "Cname" character varying(100) NOT NULL
);
    DROP TABLE public."College";
       public         heap    postgres    false    4            O           0    0    TABLE "College"    COMMENT     6   COMMENT ON TABLE public."College" IS '学院信息
';
          public          postgres    false    217            �            1259    16458    Course    TABLE     �   CREATE TABLE public."Course" (
    "Cno" character varying(8) NOT NULL,
    "Cname" character varying(100),
    "Credit" character varying(1),
    "Ctno" character varying(3),
    "Tno" character varying(8)
);
    DROP TABLE public."Course";
       public         heap    postgres    false    4            P           0    0    TABLE "Course"    COMMENT     4   COMMENT ON TABLE public."Course" IS '课程信息';
          public          postgres    false    221            �            1259    16560    MeetingRoomA    TABLE     �   CREATE TABLE public."MeetingRoomA" (
    "MRno" character varying(4) NOT NULL,
    "Ano" character varying(8),
    "MRtime" character varying(4) NOT NULL
);
 "   DROP TABLE public."MeetingRoomA";
       public         heap    postgres    false    4            Q           0    0    TABLE "MeetingRoomA"    COMMENT     L   COMMENT ON TABLE public."MeetingRoomA" IS '会议室预约管理员情况';
          public          postgres    false    229            �            1259    16540    MeetingRoomS    TABLE     �   CREATE TABLE public."MeetingRoomS" (
    "MRno" character varying(4) NOT NULL,
    "Sno" character varying(8),
    "MRtime" character varying(4) NOT NULL
);
 "   DROP TABLE public."MeetingRoomS";
       public         heap    postgres    false    4            R           0    0    TABLE "MeetingRoomS"    COMMENT     I   COMMENT ON TABLE public."MeetingRoomS" IS '会议室预约学生情况';
          public          postgres    false    227            �            1259    16550    MeetingRoomT    TABLE     �   CREATE TABLE public."MeetingRoomT" (
    "MRno" character varying(4) NOT NULL,
    "Tno" character varying(8),
    "MRtime" character varying(4) NOT NULL
);
 "   DROP TABLE public."MeetingRoomT";
       public         heap    postgres    false    4            S           0    0    TABLE "MeetingRoomT"    COMMENT     I   COMMENT ON TABLE public."MeetingRoomT" IS '会议室预约教师情况';
          public          postgres    false    228            �            1259    16515    ProjMen    TABLE     t   CREATE TABLE public."ProjMen" (
    "Pno" character varying(8) NOT NULL,
    "Sno" character varying(8) NOT NULL
);
    DROP TABLE public."ProjMen";
       public         heap    postgres    false    4            T           0    0    TABLE "ProjMen"    COMMENT     8   COMMENT ON TABLE public."ProjMen" IS '项目队员表';
          public          postgres    false    225            �            1259    16500    Project    TABLE     �   CREATE TABLE public."Project" (
    "Pno" character varying(8) NOT NULL,
    "Pname" character varying(100),
    "Sno" character varying(8),
    "Tno" character varying(8)
);
    DROP TABLE public."Project";
       public         heap    postgres    false    4            U           0    0    TABLE "Project"    COMMENT     5   COMMENT ON TABLE public."Project" IS '项目情况';
          public          postgres    false    224            �            1259    16470    Scredit    TABLE     �   CREATE TABLE public."Scredit" (
    "Sno" character varying(8) NOT NULL,
    "Cno" character varying(8) NOT NULL,
    "Pass" character varying(10)
);
    DROP TABLE public."Scredit";
       public         heap    postgres    false    4            V           0    0    TABLE "Scredit"    COMMENT     ;   COMMENT ON TABLE public."Scredit" IS '学分完成情况';
          public          postgres    false    222            �            1259    16446    Student    TABLE     �   CREATE TABLE public."Student" (
    "Sno" character varying(8) NOT NULL,
    "Skey" character varying,
    "Sname" character varying(100),
    "Grade" character varying(4),
    "Sgender" character varying(2),
    "Cono" character(2)
);
    DROP TABLE public."Student";
       public         heap    postgres    false    4            W           0    0    TABLE "Student"    COMMENT     5   COMMENT ON TABLE public."Student" IS '学生信息';
          public          postgres    false    220            �            1259    16485    Tcredit    TABLE     �   CREATE TABLE public."Tcredit" (
    "Tno" character varying(8) NOT NULL,
    "Cno" character varying(8) NOT NULL,
    "Pass" character varying(1)
);
    DROP TABLE public."Tcredit";
       public         heap    postgres    false    4            X           0    0    TABLE "Tcredit"    COMMENT     ;   COMMENT ON TABLE public."Tcredit" IS '教分完成情况';
          public          postgres    false    223            �            1259    16434    Teacher    TABLE     �   CREATE TABLE public."Teacher" (
    "Tno" character varying(8) NOT NULL,
    "Tkey" character varying,
    "Tname" character varying(100),
    "Tlevel" character varying(3),
    "Tgender" character varying(2),
    "Cono" character varying(2)
);
    DROP TABLE public."Teacher";
       public         heap    postgres    false    4            Y           0    0    TABLE "Teacher"    COMMENT     5   COMMENT ON TABLE public."Teacher" IS '教师信息';
          public          postgres    false    219            :          0    16427    Admin 
   TABLE DATA           0   COPY public."Admin" ("Ano", "Akey") FROM stdin;
    public          postgres    false    218   �O       B          0    16530 	   ClassRoom 
   TABLE DATA           F   COPY public."ClassRoom" ("CRno", "Cno", "Ctno", "CRtime") FROM stdin;
    public          postgres    false    226   �O       9          0    16422    College 
   TABLE DATA           4   COPY public."College" ("Cono", "Cname") FROM stdin;
    public          postgres    false    217   2P       =          0    16458    Course 
   TABLE DATA           K   COPY public."Course" ("Cno", "Cname", "Credit", "Ctno", "Tno") FROM stdin;
    public          postgres    false    221   �P       E          0    16560    MeetingRoomA 
   TABLE DATA           A   COPY public."MeetingRoomA" ("MRno", "Ano", "MRtime") FROM stdin;
    public          postgres    false    229   �Q       C          0    16540    MeetingRoomS 
   TABLE DATA           A   COPY public."MeetingRoomS" ("MRno", "Sno", "MRtime") FROM stdin;
    public          postgres    false    227   �Q       D          0    16550    MeetingRoomT 
   TABLE DATA           A   COPY public."MeetingRoomT" ("MRno", "Tno", "MRtime") FROM stdin;
    public          postgres    false    228   `R       A          0    16515    ProjMen 
   TABLE DATA           1   COPY public."ProjMen" ("Pno", "Sno") FROM stdin;
    public          postgres    false    225   �R       @          0    16500    Project 
   TABLE DATA           A   COPY public."Project" ("Pno", "Pname", "Sno", "Tno") FROM stdin;
    public          postgres    false    224   S       >          0    16470    Scredit 
   TABLE DATA           9   COPY public."Scredit" ("Sno", "Cno", "Pass") FROM stdin;
    public          postgres    false    222   �S       <          0    16446    Student 
   TABLE DATA           W   COPY public."Student" ("Sno", "Skey", "Sname", "Grade", "Sgender", "Cono") FROM stdin;
    public          postgres    false    220   U       ?          0    16485    Tcredit 
   TABLE DATA           9   COPY public."Tcredit" ("Tno", "Cno", "Pass") FROM stdin;
    public          postgres    false    223   �U       ;          0    16434    Teacher 
   TABLE DATA           X   COPY public."Teacher" ("Tno", "Tkey", "Tname", "Tlevel", "Tgender", "Cono") FROM stdin;
    public          postgres    false    219   ZV       �           2606    16433    Admin Admin_pkey 
   CONSTRAINT     U   ALTER TABLE ONLY public."Admin"
    ADD CONSTRAINT "Admin_pkey" PRIMARY KEY ("Ano");
 >   ALTER TABLE ONLY public."Admin" DROP CONSTRAINT "Admin_pkey";
       public            postgres    false    218            �           2606    16534    ClassRoom ClassRoom_pkey 
   CONSTRAINT     h   ALTER TABLE ONLY public."ClassRoom"
    ADD CONSTRAINT "ClassRoom_pkey" PRIMARY KEY ("CRno", "CRtime");
 F   ALTER TABLE ONLY public."ClassRoom" DROP CONSTRAINT "ClassRoom_pkey";
       public            postgres    false    226    226            �           2606    16426    College College_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public."College"
    ADD CONSTRAINT "College_pkey" PRIMARY KEY ("Cono");
 B   ALTER TABLE ONLY public."College" DROP CONSTRAINT "College_pkey";
       public            postgres    false    217            �           2606    16464    Course Course_pkey 
   CONSTRAINT     W   ALTER TABLE ONLY public."Course"
    ADD CONSTRAINT "Course_pkey" PRIMARY KEY ("Cno");
 @   ALTER TABLE ONLY public."Course" DROP CONSTRAINT "Course_pkey";
       public            postgres    false    221            �           2606    16564    MeetingRoomA MeetingRoomA_pkey 
   CONSTRAINT     n   ALTER TABLE ONLY public."MeetingRoomA"
    ADD CONSTRAINT "MeetingRoomA_pkey" PRIMARY KEY ("MRno", "MRtime");
 L   ALTER TABLE ONLY public."MeetingRoomA" DROP CONSTRAINT "MeetingRoomA_pkey";
       public            postgres    false    229    229            �           2606    16544    MeetingRoomS MeetingRoomS_pkey 
   CONSTRAINT     n   ALTER TABLE ONLY public."MeetingRoomS"
    ADD CONSTRAINT "MeetingRoomS_pkey" PRIMARY KEY ("MRno", "MRtime");
 L   ALTER TABLE ONLY public."MeetingRoomS" DROP CONSTRAINT "MeetingRoomS_pkey";
       public            postgres    false    227    227            �           2606    16554    MeetingRoomT MeetingRoomT_pkey 
   CONSTRAINT     n   ALTER TABLE ONLY public."MeetingRoomT"
    ADD CONSTRAINT "MeetingRoomT_pkey" PRIMARY KEY ("MRno", "MRtime");
 L   ALTER TABLE ONLY public."MeetingRoomT" DROP CONSTRAINT "MeetingRoomT_pkey";
       public            postgres    false    228    228            �           2606    16519    ProjMen ProjMen_pkey 
   CONSTRAINT     `   ALTER TABLE ONLY public."ProjMen"
    ADD CONSTRAINT "ProjMen_pkey" PRIMARY KEY ("Pno", "Sno");
 B   ALTER TABLE ONLY public."ProjMen" DROP CONSTRAINT "ProjMen_pkey";
       public            postgres    false    225    225            �           2606    16504    Project Project_pkey 
   CONSTRAINT     Y   ALTER TABLE ONLY public."Project"
    ADD CONSTRAINT "Project_pkey" PRIMARY KEY ("Pno");
 B   ALTER TABLE ONLY public."Project" DROP CONSTRAINT "Project_pkey";
       public            postgres    false    224            �           2606    16474    Scredit Scredit_pkey 
   CONSTRAINT     `   ALTER TABLE ONLY public."Scredit"
    ADD CONSTRAINT "Scredit_pkey" PRIMARY KEY ("Sno", "Cno");
 B   ALTER TABLE ONLY public."Scredit" DROP CONSTRAINT "Scredit_pkey";
       public            postgres    false    222    222            �           2606    16452    Student Student_pkey 
   CONSTRAINT     Y   ALTER TABLE ONLY public."Student"
    ADD CONSTRAINT "Student_pkey" PRIMARY KEY ("Sno");
 B   ALTER TABLE ONLY public."Student" DROP CONSTRAINT "Student_pkey";
       public            postgres    false    220            �           2606    16489    Tcredit Tcredit_pkey 
   CONSTRAINT     `   ALTER TABLE ONLY public."Tcredit"
    ADD CONSTRAINT "Tcredit_pkey" PRIMARY KEY ("Cno", "Tno");
 B   ALTER TABLE ONLY public."Tcredit" DROP CONSTRAINT "Tcredit_pkey";
       public            postgres    false    223    223            �           2606    16440    Teacher Teacher_pkey 
   CONSTRAINT     Y   ALTER TABLE ONLY public."Teacher"
    ADD CONSTRAINT "Teacher_pkey" PRIMARY KEY ("Tno");
 B   ALTER TABLE ONLY public."Teacher" DROP CONSTRAINT "Teacher_pkey";
       public            postgres    false    219            �           2606    16565    MeetingRoomA Admin    FK CONSTRAINT     x   ALTER TABLE ONLY public."MeetingRoomA"
    ADD CONSTRAINT "Admin" FOREIGN KEY ("Ano") REFERENCES public."Admin"("Ano");
 @   ALTER TABLE ONLY public."MeetingRoomA" DROP CONSTRAINT "Admin";
       public          postgres    false    218    229    4740            �           2606    16441    Teacher College    FK CONSTRAINT     y   ALTER TABLE ONLY public."Teacher"
    ADD CONSTRAINT "College" FOREIGN KEY ("Cono") REFERENCES public."College"("Cono");
 =   ALTER TABLE ONLY public."Teacher" DROP CONSTRAINT "College";
       public          postgres    false    217    4738    219            �           2606    16453    Student College    FK CONSTRAINT     y   ALTER TABLE ONLY public."Student"
    ADD CONSTRAINT "College" FOREIGN KEY ("Cono") REFERENCES public."College"("Cono");
 =   ALTER TABLE ONLY public."Student" DROP CONSTRAINT "College";
       public          postgres    false    220    217    4738            �           2606    16465    Course Course    FK CONSTRAINT     u   ALTER TABLE ONLY public."Course"
    ADD CONSTRAINT "Course" FOREIGN KEY ("Tno") REFERENCES public."Teacher"("Tno");
 ;   ALTER TABLE ONLY public."Course" DROP CONSTRAINT "Course";
       public          postgres    false    219    4742    221            �           2606    16480    Scredit Course    FK CONSTRAINT     u   ALTER TABLE ONLY public."Scredit"
    ADD CONSTRAINT "Course" FOREIGN KEY ("Cno") REFERENCES public."Course"("Cno");
 <   ALTER TABLE ONLY public."Scredit" DROP CONSTRAINT "Course";
       public          postgres    false    222    221    4746            �           2606    16495    Tcredit Course    FK CONSTRAINT     u   ALTER TABLE ONLY public."Tcredit"
    ADD CONSTRAINT "Course" FOREIGN KEY ("Cno") REFERENCES public."Course"("Cno");
 <   ALTER TABLE ONLY public."Tcredit" DROP CONSTRAINT "Course";
       public          postgres    false    223    221    4746            �           2606    16535    ClassRoom Course    FK CONSTRAINT     w   ALTER TABLE ONLY public."ClassRoom"
    ADD CONSTRAINT "Course" FOREIGN KEY ("Cno") REFERENCES public."Course"("Cno");
 >   ALTER TABLE ONLY public."ClassRoom" DROP CONSTRAINT "Course";
       public          postgres    false    221    226    4746            �           2606    16520    ProjMen Project    FK CONSTRAINT     w   ALTER TABLE ONLY public."ProjMen"
    ADD CONSTRAINT "Project" FOREIGN KEY ("Pno") REFERENCES public."Project"("Pno");
 =   ALTER TABLE ONLY public."ProjMen" DROP CONSTRAINT "Project";
       public          postgres    false    225    4752    224            �           2606    16475    Scredit Student    FK CONSTRAINT     w   ALTER TABLE ONLY public."Scredit"
    ADD CONSTRAINT "Student" FOREIGN KEY ("Sno") REFERENCES public."Student"("Sno");
 =   ALTER TABLE ONLY public."Scredit" DROP CONSTRAINT "Student";
       public          postgres    false    220    222    4744            �           2606    16505    Project Student    FK CONSTRAINT     w   ALTER TABLE ONLY public."Project"
    ADD CONSTRAINT "Student" FOREIGN KEY ("Sno") REFERENCES public."Student"("Sno");
 =   ALTER TABLE ONLY public."Project" DROP CONSTRAINT "Student";
       public          postgres    false    224    4744    220            �           2606    16525    ProjMen Student    FK CONSTRAINT     w   ALTER TABLE ONLY public."ProjMen"
    ADD CONSTRAINT "Student" FOREIGN KEY ("Sno") REFERENCES public."Student"("Sno");
 =   ALTER TABLE ONLY public."ProjMen" DROP CONSTRAINT "Student";
       public          postgres    false    220    4744    225            �           2606    16490    Tcredit Teacher    FK CONSTRAINT     w   ALTER TABLE ONLY public."Tcredit"
    ADD CONSTRAINT "Teacher" FOREIGN KEY ("Tno") REFERENCES public."Teacher"("Tno");
 =   ALTER TABLE ONLY public."Tcredit" DROP CONSTRAINT "Teacher";
       public          postgres    false    223    219    4742            �           2606    16510    Project Teacher    FK CONSTRAINT     w   ALTER TABLE ONLY public."Project"
    ADD CONSTRAINT "Teacher" FOREIGN KEY ("Tno") REFERENCES public."Teacher"("Tno");
 =   ALTER TABLE ONLY public."Project" DROP CONSTRAINT "Teacher";
       public          postgres    false    4742    219    224            �           2606    16555    MeetingRoomT Teacher    FK CONSTRAINT     |   ALTER TABLE ONLY public."MeetingRoomT"
    ADD CONSTRAINT "Teacher" FOREIGN KEY ("Tno") REFERENCES public."Teacher"("Tno");
 B   ALTER TABLE ONLY public."MeetingRoomT" DROP CONSTRAINT "Teacher";
       public          postgres    false    228    4742    219            �           2606    16545    MeetingRoomS s    FK CONSTRAINT     t   ALTER TABLE ONLY public."MeetingRoomS"
    ADD CONSTRAINT s FOREIGN KEY ("Sno") REFERENCES public."Student"("Sno");
 :   ALTER TABLE ONLY public."MeetingRoomS" DROP CONSTRAINT s;
       public          postgres    false    220    227    4744            :   7   x�30426153��\�'T�&b�	0���pBa"��P#�=... R�T      B   X   x�s440�4� Ð�ɎC]C.GC#��a��dW���H�&a��i�k�0�I��u<�=�P�$a
� 1��FM1�5����� |��      9   T   x�30�|�n��uӟ���t���3qq>]2����0�1����϶�=*��5�|ѹ�ٜ�Ov��X�hL�*F��� �I9`      =   �   x�M�]j�@���,F&��ֽ��!(�Q�>$!/��mJ���d~��^3�y���;��^��l�J��v�� �F<��=0��,�߭�jlS�<uP �:��T�vf7s��e1Ł��^/��W��Y���-'�1je����\3o�&b��@.	��*}�\���.(�ܢ6�J�>{�D�(/��ͩR�-��,IY���s�5OM�&v%hwP��.�I���72a]B�cwE��9      E   W   x��520�40426153�|���Pא����&h��dW���H�&h	T�i�k4�
�p>�=�P�$h
4j�b�k����� �0      C   W   x�5˱�@C�:�%(N��`��E���E�{�|�^�px2�]��c�|NX�0�Y�Kb#2m�k�^��^��u[T��;�      D   W   x�5˱�@C�:�%(N��`��E���E�{�|�^�!px2�]��ǐ��� fa����Fd��ֈ�0����붨�О�      A   B   x��� 1��R�
_��K��#��� �A2�|�&K!%i)�Iy4`s)��-ZlW��l��!�t      @   �   x�-�K
�0��Y�ܾ��bT��PkA>@P�k`Q������u�Η�r��i����+���C^g�+�Dr:o�� ��\�.�4�3��0�#�H'�x���A�x�u��:���Q���ڔY��'�:��B������l�+���v�i̷�X����t~�_:�Q�VN��}�i��i
!~}�qo      >     x�m�[r�0D�oXL��Ï�d���d,j���EZ6������W;W��-�L�VL��a�6avAnW��3+�C>=�)��l��[0���z���k==Z1S0s��N����yH?��z$;�M!g`�l���բ���ٞ��@N�fl�MXo��j�_�Y:�H&`
f`6��G��]sq��2{d�)�����	�`�]sO�I=�	�r9�܀܄������~�zd;=�)��9� ������<<nS�d�0k�s�6��k�������
PS      <   �   x�]�Mj�P���y���u/.Ɓ�Eڙ�Lg��b���f��^@����j�og`��!� է|� _��<��6�Fd���y]m��%rHF�)����.oD��)�dd����!�#
HƢ]M�%�s3"GĹɸ�\���y��Hƣ��\_�D��,y"�H&�z<J�(�4D2�l��C)�|G������RP��R���~�      ?   U   x�5ι�0C��&}{��?GL)T���Bp�=�C�!��jXe6YK��zX��HcN���-�Jcn���I��������P"3      ;   �   x�U��
A��3���xCڲaC\H[.�QKg��[د���u�|GI%˧���.j�@���<�'���J�
i�F���Z��C�X��iv�I<ҡ���C��Y��\(�}U�#�`4h��y��X:Î#f@���Z##�aMcA���f�Fˈ�Z��՟Ҹ�#;�am�5;���]�~���K�Zy���mT�։NC�̇9     