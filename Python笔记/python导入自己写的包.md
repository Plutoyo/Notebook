将模块路径加入系统路径中
import sys;
sys.path.append("路径名")
import 模块名	

当然了，这种方法存在一个大问题，就是没有避免如果存在相同的文件名会出错的问题，于是需要改进成下面的方法（当然如果只是写些小的东西，上面的就已经足够了）

```python
import sys;
if not "路径名" in sys.path:
sys.path.append("路径名")
if not 'a' in sys.modules: #这里a是模块名
a = __import__('a')
else:
eval('import a')
a = eval('reload(a)')
```

2、__init__.py
在目录中建一个文件名为__init__.py的文件，就可以直接按照路径名import模块了
有了这个文件，我们就可以导入这个目录下的文件了