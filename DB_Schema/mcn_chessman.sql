CREATE TABLE `mcn`.`mcn_chessman` (
	`id` INT NOT NULL COMMENT '아이디 ',
	`user_id` INT NULL COMMENT '유저 아이디 ',
	`type` VARCHAR(45) NULL COMMENT '케릭터 타입 ',
	`level` INT NULL COMMENT '레벨 ',
	`health` INT NULL COMMENT '체력 ',
	`ability` INT NULL COMMENT '능력 ',
	`exp` INT NULL COMMENT '경험치',
	PRIMARY KEY (`id`))
COMMENT = '캐릭터 데이터 저장';
