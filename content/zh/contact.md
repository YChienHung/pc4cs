---
title: '联系我们'
type: landing

sections:
  - block: contact-info
    content:
      title: 联系我们
      subtitle: 与我们的研究团队取得联系
      visit_title: 通讯地址
      connect_title: 联系方式
      address:
        lines:
          - 中华人民共和国浙江省宁波市
          - 镇海区蛟川街道海江大道2911号
          - 宁波东方理工大学
          - 力学与机械工程学院
          - 复杂系统感知与控制实验室
      office_hours:
        - "周一 至 周五: 9:00 至 17:30"
      map_embed: |
        <iframe
          width="100%"
          height="480"
          loading="lazy"
          allowfullscreen
          referrerpolicy="no-referrer-when-downgrade"
          src="https://www.google.com/maps?q=29.921496,121.663737&z=14&output=embed&hl=zh-CN"
          style="border: 0;"
        </iframe>
      email: lab@example.edu
      phone: "+1 (555) 123-4567"
      social:
        - icon: brands/xiaohongshu
          color: "#FF2442"
          url: https://www.xiaohongshu.com/user/profile/5ceaa056000000001000d2d4
        - icon: brands/zhihu
          color: "#0084FF"
          url: https://www.zhihu.com/
        - icon: brands/github
          color: "#181717"
          url: https://www.github.com/
        - icon: brands/bilibili
          color: "#00A1D6"
          url: https://www.bilibili.com/
      prospective:
        title: 招募成员
        text: 我们欢迎对科研充满热情、勇于探索的伙伴加入实验室，一同开展创新研究，解决具有挑战性的科学与工程问题。
        button:
          text: 查看招募岗位
          url: /join
      show_form: false
    design:
      # css_class: "bg-gray-50 dark:bg-gray-900"
      spacing:
        padding: ["3rem", 0, "3rem", 0]

---
<!-- 
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>点标记的拖拽</title>
<link rel="stylesheet" href="https://mapopen-docs-jsdemo.bj.bcebos.com/jsdemo/assets/iframe-ui-CXHGEBD7.css">
<script src="https://api.map.baidu.com/api?v=4.0&ak=您的密钥"></script>
<style>
html,
body,
#map {
  width: 100%;
  height: 100%;
  margin: 0;
}

</style>
</head>
<body>
<div id="map"></div>
<div class="operate">
  <button onclick="marker.enableDragging()">可拖拽</button>
  <button onclick="marker.disableDragging()">不可拖拽</button>
</div>

<script>
// 百度地图API功能
var map = new BMap.Map('map');
var point = new BMap.Point(121.6716, 29.9283);
map.centerAndZoom(point, 18);
var marker = new BMap.Marker(point, {
  // 启用拖拽
  enableDragging: true,
}); // 创建标注
map.addOverlay(marker); // 将标注添加到地图中

</script>
</body>
</html> -->