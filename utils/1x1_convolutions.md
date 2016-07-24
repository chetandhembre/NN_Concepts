#1x1 convolutions

![1x1 convolution](https://raw.githubusercontent.com/iamaaditya/iamaaditya.github.io/master/images/conv_arithmetic/full_padding_no_strides_transposed_small.gif)

above gif explained how 1x1 convolution works.

##Purpose

- Dimension reduction
  we basically reduce feature map of input i.e. depth of input
  ```
   for example lets consider if we have layer with size (200 x 200 x 50) and then we apply 1x1 convolution filter with k = 20 then we will get o/p with (200 x 200 x 20), which is significant dimension reduction and it actually destroy very less information.
  ```


