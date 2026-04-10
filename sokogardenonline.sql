-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 25, 2026 at 10:07 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.1.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sokogardenonline`
--

-- --------------------------------------------------------

--
-- Table structure for table `product_details`
--

CREATE TABLE `product_details` (
  `product_id` int(50) NOT NULL,
  `product_name` varchar(100) NOT NULL,
  `product_description` varchar(2000) NOT NULL,
  `product_cost` int(50) NOT NULL,
  `product_photo` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `product_details`
--

INSERT INTO `product_details` (`product_id`, `product_name`, `product_description`, `product_cost`, `product_photo`) VALUES
(1, 'Android phone', 'very good', 20000, '<FileStorage: \'download.jpg\' (\'image/jpeg\')>'),
(2, 'Android phone', 'very good', 20000, 'download.jpg'),
(3, 'Smart watch', 'Cool and size strap', 20000, 'smartwatch.jpg'),
(6, 'Headphones', 'comfortable and 100%JBL product', 3500, 'headphones-jbl.jpg'),
(7, 'Iphone 14', 'New features', 52000, 'iphone 14 acessories.jpg'),
(8, 'Router', 'High Quality', 5000, 'router.com_what-is-the-wps-button-on-my-router_'),
(10, 'Laptop', ' High quality laptop', 32000, 'MacBook Pro 16-inch Silver Mockup.jpg'),
(11, 'Pods', 'Power lasting ', 1100, 'pods.jpg'),
(12, 'Pods', 'Power lasting ', 1100, 'pods.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(50) NOT NULL,
  `username` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `username`, `email`, `phone`, `password`) VALUES
(1, 'misheck', 'misheck@gmail.com', '0741588020', '1234'),
(2, 'misheck', 'misheck@gmail.com', '0741588020', '1234'),
(3, 'dan', 'misheck@gmail.com', '0741588020', '1234'),
(4, 'misheck karani', 'karanimisheck22@gmail.com', '0741588020', 'scrypt:32768:8:1$sxgHpALiHg39Y2LS$76e267b17230487c0cb84e7de97f24c2f555241cbddfe8a7f8c871ba3ff59e87bf'),
(5, 'misheck karani', 'karanimisheck22@gmail.com', '0741588020', 'scrypt:32768:8:1$u7d40WV9Y5PXac27$55681f5d1269bd89cab080aafe9e309230d92b29d02ed50278c7c34cefba12df9e'),
(6, 'misheck karani', 'karanimisheck22@gmail.com', '0741588020', 'scrypt:32768:8:1$APEhAtBfjy97i3ix$5f67f3311eff8a5cee397ef624988c2c96bfa575b663283a6cdef66554cfd95cb4'),
(7, 'misheck karani', 'karanimisheck22@gmail.com', '0741588020', 'scrypt:32768:8:1$1v6biLERkwY2Z0b9$e1f261efb64a7dccaf4be4bb14defef6380df3aa145edb3e28f06f7ca168169adc');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `product_details`
--
ALTER TABLE `product_details`
  ADD PRIMARY KEY (`product_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `product_details`
--
ALTER TABLE `product_details`
  MODIFY `product_id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
