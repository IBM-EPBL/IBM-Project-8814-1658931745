{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 373
        },
        "id": "pmtu-3VrxKZk",
        "outputId": "a32c4921-30cb-433e-d506-f5fd7ab18b94"
      },
      "outputs": [
        {
          "output_type": "error",
          "ename": "ImportError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mImportError\u001b[0m                               Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-1-d31f0914475f>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mnumpy\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mnp\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mkeras\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmodels\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 3\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0mscipy\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmisc\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mimread\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mimresize\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mimshow\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      4\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mtensorflow\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mtf\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mImportError\u001b[0m: cannot import name 'imread' from 'scipy.misc' (/usr/local/lib/python3.7/dist-packages/scipy/misc/__init__.py)",
            "",
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0;32m\nNOTE: If your import is failing due to a missing package, you can\nmanually install dependencies using either !pip or !apt.\n\nTo view examples of installing some common dependencies, click the\n\"Open Examples\" button below.\n\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n"
          ],
          "errorDetails": {
            "actions": [
              {
                "action": "open_url",
                "actionText": "Open Examples",
                "url": "/notebooks/snippets/importing_libraries.ipynb"
              }
            ]
          }
        }
      ],
      "source": [
        "import numpy as np\n",
        "import keras.models\n",
        "from scipy.misc import imread, imresize,imshow\n",
        "import tensorflow as tf\n",
        "\n",
        "from keras.models import Sequential\n",
        "from keras.models import Sequential\n",
        "from keras.layers import Dense, Dropout, Flatten\n",
        "from keras.layers import Conv2D, MaxPooling2D\n",
        "\n",
        "def init():\n",
        "    num_classes = 10\n",
        "    img_rows, img_cols = 28, 28\n",
        "    input_shape = (img_rows, img_cols, 1)\n",
        "    model = Sequential()\n",
        "    model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=input_shape))\n",
        "    model.add(Conv2D(64, (3, 3), activation='relu'))\n",
        "    model.add(MaxPooling2D(pool_size=(2, 2)))\n",
        "    model.add(Dropout(0.25))\n",
        "    model.add(Flatten())\n",
        "    model.add(Dense(128, activation='relu'))\n",
        "    model.add(Dropout(0.5))\n",
        "    model.add(Dense(num_classes, activation='softmax'))\n",
        "    \n",
        "    #load woeights into new model\n",
        "    model.load_weights(\"weights.h5\")\n",
        "    print(\"Loaded Model from disk\")\n",
        "\n",
        "    #compile and evaluate loaded model\n",
        "    model.compile(loss=keras.losses.categorical_crossentropy, optimizer=keras.optimizers.Adadelta(), metrics=['accuracy'])\n",
        "    #loss,accuracy = model.evaluate(X_test,y_test)\n",
        "    #print('loss:', loss)\n",
        "    #print('accuracy:', accuracy)\n",
        "    graph = tf.get_default_graph()\n",
        "\n",
        "    return model, "
      ]
    }
  ]
}