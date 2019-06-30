# QOpenGL使用心得

##　使用步骤

- 创建QOpenGLWidget对象

  ``` python
  class CGLWidget(QtWidgets.QOpenGLWidget)
  ```

  

- 设置OpenGL版本，并获取对应版本的OpenGL函数集

  ``` python
  def __init__(self):
  	_format = QtGui.QSurfaceFormat()
  	_format.setVersion(4, 1)
  	_format.setProfile(QtGui.QSurfaceFormat.CoreProfile)
  	_format.setSample(4)
  	QtGui.QSurfaceFormat.setDefaultFormat(_format)
  	version_profile = QtGui.QOpenGLVersionProfile()
  	version_profile.setVersion(4, 1)
  	version_profile.setProgile(QtGui.QSurfaceFormat.CoreProfile)
  	self.gl = self.context().versionFunctions(version_progile)
  ```

- 