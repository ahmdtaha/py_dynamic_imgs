import dynamic_image_generator
import cv2

def example2():
    imgs_lst = []
    for i in range(8, 18):
        imgs_lst.append('./sample_images/frame' + '%05d' % i + '.jpg')
    return imgs_lst

def example1():
    imgs_lst = []
    for i in range(169, 174):
        imgs_lst.append('./sample_images/frame_' + '%05d' % i + '.jpg')
    return imgs_lst

if __name__ == '__main__':

    dyn_img_gen = dynamic_image_generator.DynamicImageGenerator();

    imgs_lst = example2()
    result_dyn_img = dyn_img_gen.approximate_dynamic_image(imgs_lst, uint8_normalize=True);
    cv2.imwrite('./sample_images/dyn_img.png', result_dyn_img)


