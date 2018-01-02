import cv2
import numpy as np


class DynamicImageGenerator:


    def approximate_dynamic_image(self,imgs_lst,uint8_normalize = False):
        num_imgs = len(imgs_lst)
        rgb_imgs = []
        for i in range(num_imgs):
            bgr = cv2.imread(imgs_lst[i]);
            if(len(bgr.shape) == 2):
                rgb_imgs.append(bgr) ## It is gray
            else:
                rgb_imgs.append(cv2.cvtColor(bgr ,cv2.COLOR_BGR2RGB))

        alpha_weights = np.zeros(num_imgs)
        for i in range(num_imgs):
            num = (2 * np.arange(i+1,num_imgs+1) - num_imgs -1)
            den = np.arange(i+1,num_imgs+1)
            alpha_weights[i] = np.sum(num / den)

        template_shape = rgb_imgs[0].shape ## assume all images have same shape
        result_dynamic_image = np.zeros(template_shape)

        for i in range(num_imgs):
            result_dynamic_image += rgb_imgs[i].astype(np.float32) * alpha_weights[i];

        if uint8_normalize:
            result_dynamic_image = result_dynamic_image - np.amin(result_dynamic_image)
            result_dynamic_image = 255 * result_dynamic_image / np.amax(result_dynamic_image);

        return result_dynamic_image



