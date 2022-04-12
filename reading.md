

## Kindle note export

增加换行
```
cat nanke.md | grep -v "标注" | grep -v "导出" | sed -z 's/\n/\n\n/g' >~/nanke_sed.md
```

