#!/bin/bash


#Function of setting configuration
set_conf() {
	echo "Enter your username for git"
	read name
	git config --global user.name "$name"
	
	echo "Enter your email for git"
	read mail
	git config --global user.email "$mail"
}


#Install Git and set configuration
if command -v git &> /dev/null; then
	echo "Git is already installed"
	
	if [ -z "$(git config user.name)" ]; then
		echo -e "\nSetting configuration"
		set_conf
	fi

else
	echo "Installing git..."
	sudo apt update
	sudo apt install -y git
	
	echo -e "\nGit has successfully installed"

	echo -e "\nSetting configuration"
	set_conf
fi

git --version


#Make an alias command
echo -e "\nMaking an alias..."

if [ -z "$(grep "alias gitv='git --version'" ~/.bashrc)" ]; then
	echo "alias gitv='git --version'" >> ~/.bashrc
	source ~/.bashrc
fi

echo "Now you can check the version of git typing 'gitv' instead of 'git --version'"
