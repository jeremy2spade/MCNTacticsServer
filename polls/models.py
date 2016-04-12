# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models

class User(models.Model):
	user_id = models.CharField(max_length=20) #유저 아이디 
	passwd = models.CharField(max_length=100) #패스워드 
	name = models.CharField(max_length=30) #유저명 
	email = models.CharField(max_length=200) #메일 
	created_ymd = models.DateTimeField('date published') # 생성일 
	conn_status = models.CharField(max_length=15) # 접속상태 

	def __unicode__(self):
		return self.user_id +"/"+self.conn_status

class Chessman(models.Model):
	user_id = models.CharField(max_length=20) #유저아이디 
	type = models.CharField(max_length = 45) # 케릭터 타입 
	level = models.IntegerField() # 레벨 
	health = models.IntegerField() # 체력 
	ability = models.IntegerField() # 능력 
	exp = models.IntegerField() # 경험치
	
	def __unicode__(self):
		return self.user_id +"/"+ self.type


