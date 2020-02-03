all:
# clean python_depencies preprocess_dataset

clean:
	rm -r cache/

linux_dependencies:
	sudo apt update
	sudo apt upgrade
	sudo apt install cmake
	sudo apt install python3-pip
	sudo apt autoclean
	sudo apt autoremove

setup_cuda:
	#echo "ok"
	sudo -H pip3 uninstall tensorflow-gpu
	sudo -H pip3 install --upgrade tensorflow-gpu==1.12.2
	#sudo -H pip3 install --upgrade tensorflow-gpu==1.10.0  ## Hopefull
	#sudo -H pip3 install --upgrade tensorflow-gpu
	#sudo -H pip3 install tensorflow-gpu==1.9.0
	#wget "https://developer.nvidia.com/compute/cuda/9.0/Prod/local_installers/cuda-repo-ubuntu1604-9-0-local_9.0.176-1_amd64-deb"
	#sudo dpkg -i cuda-repo-ubuntu1604-9-0-local_9.0.176-1_amd64-deb
	#sudo apt-key add /var/cuda-repo-9-0-local/7fa2af80.pub
	#sudo apt update
	#sudo apt install cuda=9.0.176-1



github_dependencies:
	git clone https://github.com/pbaylies/stylegan-encoder

python_depencies:
	sudo -H pip3 install -r requirements.txt

preprocess_dataset:
	mkdir -p cache/processed/
	python3 preprocess.py ../rawdata/bu3dfe/png_files/ cache/processed/
align_dataset:
	mkdir -p cache/aligned/
	python3 stylegan-encoder/align_images.py cache/processed/ cache/aligned/ --output_size=1024
encode_dataset:
	python3 stylegan-encoder/encode_images.py --face_mask=True --batch_size=1 \
	--output_video=False --load_resnet={resnet_path} --lr=0.01 --decay_rate=0.8 \
	--iterations=100 --use_l1_penalty=0.1 cache/aligned_test/ cache/reconstructions/ \
	cache/dlatents --model_url "https://drive.google.com/uc?id=1MEGjdvVpUsu1jB4zrXZN7Y4kBBOzizDQ"

cudnn_version:
	locate cudnn | grep "libcudnn.so." | tail -n1 | sed -r 's/^.*\.so\.//'
