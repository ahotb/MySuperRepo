--- انشاء قاعدة بيانات للمشروع 
CREATE DATABASE IF NOT EXISTS `hbbnb`;

USE `hbbnb`;

-- انشاء الجدول الاول للمستخدمين
CREATE TABLE
	IF NOT EXISTS `users` (
		`id` INT NOT NULL AUTO_INCREMENT, -- يعطي ترقيم تلقائي 
		`username` VARCHAR(255) NOT NULL,
		`email` VARCHAR(255) NOT NULL,
		`password` VARCHAR(255) NOT NULL,
		`role_owner` BOOLEAN DEFAoLT FALSE, -- لتحديد  الصلاحيات ويكون تلقائي لاتوجد صلاحيات 
		`role_admin` BOOLEAN DEFAoLT FALSE,
		PRIMARY KEY (`id`) -- ليكون الرقم فريد ولايتكرر 
	);

CREATE TABLE
	IF NOT EXISTS `amenity` (
		`id` INT NOT NULL AUTO_INCREMENT,
		`description` VARCHAR(255) NOT NULL,
		`images` VARCHAR(255),
		PRIMARY KEY (`id`)
	);

CREATE TABLE
	IF NOT EXISTS `Place` (
		`id` INT NOT NULL AUTO_INCREMENT,
		`title` VARCHAR(255) NOT NULL,
		`description` TEXT,
		`price` INT NOT NULL,
		`location` INT NOT NULL,
		`Amenity_id` INT,
		`user_id` INT,
		FOREIGN KEY (Amenity_id) REFERENCES Amenity (id), -- ربط العلاقات بين الجداول 
		FOREIGN KEY (user_id) REFERENCES users (id),
		PRIMARY KEY (`id`)
	);

CREATE TABLE
	IF NOT EXISTS `review` (
		`id` INT NOT NULL AUTO_INCREMENT,
		`comment` TEXT,
		`rating` INT NOT NULL CHECK (rating BETWEEN 1 AND 5),
		`user_id` INT,
		`place_id` INT,
		FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE ON UPDATE RESTRICT, -- للحذف وعدم تحديث المدخلات 
		--  ON UPDATE RESTRICT هذا يمنع التحديث 
		FOREIGN KEY (place_id) REFERENCES Place (id),
		PRIMARY KEY (`id`)
	);