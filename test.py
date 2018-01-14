import re

s1 = '''USE [123]
GO
/****** Object:  Table [dbo].[T3_Fault]    Script Date: 14.01.2018 18:07:13 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[T3_Fault](
	[Fault_id] [int] NOT NULL,
	[Fault_type] [varchar](100) NOT NULL,
	[Punishment] [varchar](100) NULL,
	[Prisoner_ID] [int] NOT NULL,
 CONSTRAINT [T3_Fault_PK] PRIMARY KEY CLUSTERED 
(
	[Fault_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[T3_Guard]    Script Date: 14.01.2018 18:07:14 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[T3_Guard](
	[Guard_id] [int] NOT NULL,
	[name] [varchar](15) NOT NULL,
 CONSTRAINT [T3_Guard_PK] PRIMARY KEY CLUSTERED 
(
	[Guard_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[T3_Prisoner]    Script Date: 14.01.2018 18:07:14 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[T3_Prisoner](
	[Prisoner_ID] [int] NOT NULL,
	[Block_number] [int] NOT NULL,
	[Room_number] [int] NULL,
	[Name] [varchar](50) NOT NULL,
	[Item_list] [int] NOT NULL,
 CONSTRAINT [T3_Prisoner_PK] PRIMARY KEY CLUSTERED 
(
	[Prisoner_ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[T3_Report]    Script Date: 14.01.2018 18:07:14 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[T3_Report](
	[Report_id] [int] NOT NULL,
	[Text] [varchar](500) NOT NULL,
	[Time] [varchar](10) NOT NULL,
	[Guard_id] [int] NOT NULL,
 CONSTRAINT [T3_Report_PK] PRIMARY KEY CLUSTERED 
(
	[Report_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[T3_Timetable]    Script Date: 14.01.2018 18:07:14 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[T3_Timetable](
	[Timetable_id] [int] NOT NULL,
	[Monday_time] [varchar](15) NOT NULL,
	[Tuesday_time] [varchar](15) NOT NULL,
	[Wednesday_time] [varchar](15) NOT NULL,
	[Thursday_time] [varchar](15) NOT NULL,
	[Friday_time] [varchar](15) NOT NULL,
	[Saturday_time] [varchar](15) NOT NULL,
	[Sunday_time] [varchar](15) NOT NULL,
	[Guard_id] [int] NULL,
 CONSTRAINT [T3_Timetable_PK] PRIMARY KEY CLUSTERED 
(
	[Timetable_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[T3_Visit]    Script Date: 14.01.2018 18:07:14 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[T3_Visit](
	[Visit_id] [int] NOT NULL,
	[Visitor_name] [varchar](50) NULL,
	[Data] [varchar](50) NULL,
	[Time] [varchar](10) NULL,
	[Guard_id] [int] NOT NULL,
	[Prisoner_id] [int] NOT NULL,
 CONSTRAINT [T3_Visit_PK] PRIMARY KEY CLUSTERED 
(
	[Visit_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[T3_Fault]  WITH CHECK ADD  CONSTRAINT [FK_T3_Fault_Prisoner] FOREIGN KEY([Prisoner_ID])
REFERENCES [dbo].[T3_Prisoner] ([Prisoner_ID])
GO
ALTER TABLE [dbo].[T3_Fault] CHECK CONSTRAINT [FK_T3_Fault_Prisoner]
GO
ALTER TABLE [dbo].[T3_Report]  WITH CHECK ADD  CONSTRAINT [FK_T3_Report_Guard] FOREIGN KEY([Guard_id])
REFERENCES [dbo].[T3_Guard] ([Guard_id])
GO
ALTER TABLE [dbo].[T3_Report] CHECK CONSTRAINT [FK_T3_Report_Guard]
GO
ALTER TABLE [dbo].[T3_Timetable]  WITH CHECK ADD  CONSTRAINT [FK_T3_Timetable_Guard] FOREIGN KEY([Guard_id])
REFERENCES [dbo].[T3_Guard] ([Guard_id])
GO
ALTER TABLE [dbo].[T3_Timetable] CHECK CONSTRAINT [FK_T3_Timetable_Guard]
GO
ALTER TABLE [dbo].[T3_Visit]  WITH CHECK ADD  CONSTRAINT [FK_T3_Visit_Guard] FOREIGN KEY([Guard_id])
REFERENCES [dbo].[T3_Guard] ([Guard_id])
GO
ALTER TABLE [dbo].[T3_Visit] CHECK CONSTRAINT [FK_T3_Visit_Guard]
GO
ALTER TABLE [dbo].[T3_Visit]  WITH CHECK ADD  CONSTRAINT [FK_T3_Visit_Prisoner] FOREIGN KEY([Prisoner_id])
REFERENCES [dbo].[T3_Prisoner] ([Prisoner_ID])
GO
ALTER TABLE [dbo].[T3_Visit] CHECK CONSTRAINT [FK_T3_Visit_Prisoner]
GO
'''

t = re.split(r".*\*\*\*.*", s1)

for i in range(1, len(t) - 1):
	t[i] = "GO\n" + t[i]
	s1 = t[i]
	s2 = re.sub(r"[\[\]]", "", s1)
	s2 = re.sub(r"GO(.*\n)*CREATE", "CREATE", s2)
	s2 = re.sub(r"dbo\.", "", s2)
	s2 = re.sub(r"CLUSTERED\s*\(\s*([\w_]*)(.*\n)\)(.*\n)(.*\n)", "(\g<1>)\n)\n;", s2)
	s2 = re.sub(r"GO", "", s2)
	s2 = s2.replace("int", "INTEGER").replace("varchar", "VARCHAR")
	print (s2)

t = re.split(r"ALTER", t[-1])
t[0] = "GO\n" + t[0]
s1 = t[0]
s2 = re.sub(r"[\[\]]", "", s1)
s2 = re.sub(r"GO(.*\n)*CREATE", "CREATE", s2)
s2 = re.sub(r"dbo\.", "", s2)
s2 = re.sub(r"CLUSTERED\s*\(\s*([\w_]*)(.*\n)\)(.*\n)(.*\n)", "(\g<1>)\n)\n;", s2)
s2 = re.sub(r"GO", "", s2)
s2 = s2.replace("int", "INTEGER").replace("varchar", "VARCHAR")
print (s2)

for i in range(1, len(t)):
	t[i] = "ALTER" + t[i]
	s2 = re.sub(r"[\[\]]", "", t[i])
	s2 = re.sub(r"dbo\.", "", s2)
	s2 = re.sub(r"GO\n", "", s2)
	s2 = s2.replace(" WITH CHECK ", "")
	print (s2 + ";")

'''ALTER TABLE T3_Fault ADD CONSTRAINT FK_T3_Fault_Prisoner
    FOREIGN KEY (Prisoner_id)
    REFERENCES T3_Prisoner(Prisoner_id)
;'''