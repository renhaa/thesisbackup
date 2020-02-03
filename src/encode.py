def encode():
    !mkdir -p pretrained_models/

    # if not os.path.isfile(resnet_path):
    #     gdown.download(resnet_url,resnet_path,quiet=False)

    # if not os.path.isfile(stylegan_ffhq_path):
    #     gdown.download(stylegan_ffhq_url,stylegan_ffhq_path,quiet=False)

    # !python stylegan-encoder/encode_images.py --face_mask=True --batch_size=4 --output_video=False --load_resnet={resnet_path} --lr=0.1 --decay_rate=0.8 --iterations=200 --use_l1_penalty=0.1 thesis_aligned_imgs/ generated_images_dir/ thesis_dlatent/
    !python3 stylegan-encoder/encode_images.py --face_mask=True --batch_size=8 --load_resnet={resnet_path} --lr=0.01 --decay_rate=0.8 --iterations=100 --use_l1_penalty=0.1 thesis_aligned_imgs/ /tmp/generated tmp/dlatents/

src_dir = "thesis_aligned_imgs"
generated_images_dir = "thesis_reconstruction"
dlatent_dir = "thesis_dlatent"
resnet_url = "https://drive.google.com/uc?id=1aT59NFy9-bNyXjDuZOTMl0qX0jmZc6Zb"
resnet_path = "pretrained_models/finetuned_resnet.h5"
stylegan_ffhq_url = "https://drive.google.com/uc?id=1MEGjdvVpUsu1jB4zrXZN7Y4kBBOzizDQ"
# stylegan_ffhq_path = "InterFaceGAN/models/pretrain/karras2019stylegan-ffhq-1024x1024.pkl"
stylegan_ffhq_path = "pretrained_models/karras2019stylegan-ffhq-1024x1024.pkl"
