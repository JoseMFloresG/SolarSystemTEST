# UUV_dev_docker
### Proceso necesario para la instalacion

## Requerimientos iniciales ###

-Particion de Linux
-Docker
    
## Instalacion de Docker ###

   -Los pasos vienen en la siguiente pagina [Docker Installation](https://docs.docker.com/engine/install/ubuntu/)
    
## Recomendaciones Docker ###

   -En VS Code tienen su propia extension que te permitira ver tus contenedores
    
## Instalacion Nvidia - Docker2 ###

-Seguir los pasos descritos en la siguiente pagina: [Nvidia installation](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html)
-Abrir en Ubuntu Apps Software & Updates
-Entrar en Additional Drivers
-Seleccionar lo siguiente: ![Nvidia Drivers]()
    
### Si no tienes tarjeta nvidia correr en lugar del uuv.build ###

-Cambiar dentro del Makefile la version de ros por melodic.
-Escribe los siguientes comandos:
```
chmod +x runIntelGpu.bash
sudo make uuv.intelcreate
```
-Comentar el run Pangolin en el Dockerfile
    
## Posible error de drivers ###

-Revisar que si allan instalado los drivers correctos
-Desactivar secure boot en la BIOS

## Clonacion del repositorio ###

-Abrir Github e ir a la configuracion de tu perfil
-Ir a Developer settings
-Entrar a Tokens (classic) dentro de Personal access tokens
-Generar un token. (Tendras que seleccionar los permisos que te quieras dar, selecciona todos, menos el de borrar repositorios)
-Ir al siguiente repositorio ![UV_dev_docker](https://github.com/vanttec/UV_dev_docker)
-Ahora deberas crearte una cuenta de docker en la siguiente pagina: ![DOCKER](https://hub.docker.com/signup)
-Abres una terminal en linux e ingresas los siguiente comandos:
 En el usuario escribe tu usuario de Github y en contrasena la password que generaste
    
```
sudo docker login
```
-Vas a clonar el siguiente repo: ![Repo UV_dev_docker](https://github.com/vanttec/UV_dev_docker)
```
sudo make uuv.build
```
-A partir de aqui sigue los pasos descritos en el repositorio

## Repositorios a descargar ###
    
-Abre una nueva terminal
-Estos repositorios tendran que ser clonados dentro del /ws/src
-Entra a la carpeta con los siguiente comandos
```
cd /ws/src
```

-darknet_ros_zed (Paquete que nos permite usar YOLO)
```
git clone --recursive https://github.com/vanttec/darknet_ros.git
```
-octomap_mapping (Paquete para mapeo)
```
git clone https://github.com/vanttec/octomap_mapping
```
-vanttec_uuv
```
git clone https://github.com/vanttec/vanttec_uuv 
cd vanttec_uuv
git checkout retos
cd ../
```
-vehicle_user_control
```
git clone https://github.com/vanttec/vehicle_user_control
```

-Para los siguientes vamos a salir de la carpeta src
```
cd ../
```
-Seguiran los pasos de instalacion de la seccion Build with opencv_contrib de esta pagina: [OpenCV](https://docs.opencv.org/4.x/d7/d9f/tutorial_linux_install.html)
-Antes de hacer catkin_make borra las carpeta de build y devel
-Para poder hacer catkin_make primero hay que sourcear la terminal
```
source /ws/devel/setup.bash
```

## Configuraciones iniciales ###

Si estas usando DOCKER
    -Dentro de la carpeta root edita el archivo .bashrc y agrega las siguientes lineas al final
```
source /ws/devel/setup.bash
export SVGA_VGPU10=0
```

## Herramientas de compilacion ###

```
sudo apt-get install python3-catkin-tools
```
-El comando para compilar es
```
catkin build
```

## Librerias necesarias ###
```
sudo apt-get install ros-melodic-octomap ros-melodic-octomap-mapping  ros-melodic-octomap-msgs ros-melodic-octomap-ros ros-melodic-octomap-rviz-plugins ros-melodic-octomap-server

sudo apt-get install ros-melodic-octomap-ros

sudo apt install ros-melodic-tf2-geometry-msgs

sudo apt-get install libsdl1.2-dev

sudo apt-get install libsdl1.2debian

sudo apt-get install ros-melodic-gazebo-plugins

sudo apt-get install ros-melodic-gazebo-ros-pkgs

sudo apt-get install ros-melodic-robot-state-publisher

sudo apt-get install ros-melodic-xacro

```

## Archivos faltantes ###

-Colocar el bootlegger.jpg y el gmangate.jpg en vanttec_uv_sim/uv_worlds/models/gate1
-Colocar el camera2.yaml en octomap_mapping/octomap_server/cfg/common
-Colocar el RoboSub2021.launch en darknet_ros/launch
-El cual requiere poner el robosub_2021_tiny3.cfg en darknet_ros/yolo_network_config/cfg 
-Colocar robosub2021_96_98.weights en darknet_ros/yolo_network_config/weights

## Librerias faltantes o que requieren versiones anteriores ###

```
sudo apt-get install python3-rospkg

sudo apt install python3-pandas

sudo apt install python-pip

sudo apt-get install python3-sklearn

pip3 install numpy==1.18

pip3 install scipy==1.1.0

pip3 install scikit-learn==0.21.3

pip3 install joblib==1.0.0

pip3 install --upgrade opencv-python
pip3 install opencv-contrib-python 
pip install opencv-contrib-python
pip install opencv-python
pip install imutils

```

## Know issues ###

Error: El submarino se carga en la superficie en lugar de bajo el agua.
Solución: Comentar la línea 4 del rviz.launch ubicado en /ws/src/vanttec_uuv/launch.

Error: darknet_ros imprime “waiting for image” y no carga YOLO.
Solución: Dentro de /ws/src/darknet_ros/darknet_ros/config/ros.yaml en la línea 4 sustituir “/camera/rgb/image_raw” por “/invert_image” y dentro de  /ws/src/darknet_ros/darknet_ros/launch/RoboSub2021.launch en la línea 26 cambiar el default por “false”.

# Instrucciones para correr el simulador

## Si lo estas corriendo localmente en cada terminal ejecuta el siguiente comando al inicio: ###
```
source devel/setup.bash
```

Cada comando se tiene que ejecutar en una terminal nueva:

```
roscore

rosrun rviz rviz

roslaunch uv_worlds lake.launch

roslaunch vehicle_descriptions vtec_u3.launch 

rosrun vehicle_descriptions gazebo_interface

roslaunch vanttec_uuv uuv_simulation.launch 


roslaunch uv_worlds task_obstacles.launch 

roslaunch octomap_server octomap_tracking_server.launch 

rosrun octomap_server uuv_octomap.py
 
rosrun octomap_server oclust_aserver.py

rosrun vanttec_uuv yolo_zed.py

```

## Control manual dentro de la simulacion ###

    -"e" para activar el control manual.
    -"w,a,s,d" para moverse en el simulador

## Para crear coordenadas: ###

En Rviz, seleccionar publish point y dar click donde se desea colocar la coordenada
![Simulador Rviz]()
Para ver en donde esta, en una terminal dentro del container correr:
```
rostopic echo /clicked_point
```    

## Instrucciones para compilar OpenCV
```
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-ubuntu2204.pin 

sudo mv cuda-ubuntu2204.pin /etc/apt/preferences.d/cuda-repository-pin-600

sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/3bf863cc.pub

sudo apt install software-properties-common

sudo add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/ /"

sudo apt-get update

sudo apt-get install libcudnn8=8.6.0.163-1+cuda11.8

sudo apt-get install libcudnn8-dev=8.6.0.163-1+cuda11.8
```

Luego hay que crear una carpeta build dentro de la carpeta de opencv y correr esto:
```
cmake -D CMAKE_BUILD_TYPE=RELEASE \
	-D CMAKE_INSTALL_PREFIX=/usr/local \
	-D INSTALL_PYTHON_EXAMPLES=ON \
	-D INSTALL_C_EXAMPLES=OFF \
	-D OPENCV_ENABLE_NONFREE=ON \
	-D WITH_CUDA=ON \
	-D WITH_CUDNN=ON \
	-D OPENCV_DNN_CUDA=ON \
	-D ENABLE_FAST_MATH=1 \
	-D CUDA_FAST_MATH=1 \
	-D CUDA_ARCH_BIN=7.5 \
	-D WITH_CUBLAS=1 \
	-D OPENCV_EXTRA_MODULES_PATH=/ws/opencv_contrib/modules \
	-D HAVE_opencv_python3=ON \
	-D PYTHON_EXECUTABLE=~/.virtualenvs/opencv_cuda/bin/python \
	-D BUILD_EXAMPLES=ON ..
```

Continuamos corriendo:
```
pip install --upgrade opencv-python
```

## Knowledge errors ###

Error: Error response from daemon: failed to create shim task: OCI runtime create failed: runc create failed: unable to start container process: error during container init: error running hook #0: error running hook: exit status 1, stdout: , stderr: Auto-detected mode as 'legacy'

Solucion:
Correr los siguientes comandos
```
sudo apt install libnvidia-cfg1-515
sudo nvidia-persistenced --user USER #reemplaza USER con tu nombre de usuario de Ubuntu
sudo nvidia-smi
```

    


