CREATE TABLE `mcn`.`mcn_user` (
	`id` INT NOT NULL AUTO_INCREMENT COMMENT '아이디 ',
	`user_id` VARCHAR(20) NULL COMMENT '유저 아이디 ',
	`passwd` VARCHAR(100) NULL COMMENT '패스워드 (암호화할것)',
	`name` VARCHAR(30) NULL COMMENT '유저명(닉네임)',
	`email` VARCHAR(200) NULL COMMENT '메일 ',
	`created_ymd` DATE NULL COMMENT '생성일 ',
	`conn_status` VARCHAR(15) NULL DEFAULT 'unreached' COMMENT '접속상태 ',
	PRIMARY KEY (`id`))
COMMENT = '유저 데이터 저장 ';
