<!-- entry point -->

<template>
  <div id="app">
    <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
    <!-- <HelloWorld msg="!!!!!!!!!!!!11Welcome to Your Vue.js App"/> -->
    <Theme v-for="(theme, key) in themes_data"
           :key="key"
           :name="key"
           :theme="theme"
    />
    <!-- <pre>{{themes_data}}</pre> -->
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import Theme from './components/Theme.vue'

export default {
  name: 'app',
  data: function(){
    /* debugger */
    /* var themes_data = {
     *   "red": {
     *     "sink": {"fg": "red", "bg": "darkred", "bold": false, "italic": false, "underline": false},
     *     "virt": {"fg": "208", "bg": "52", "bold": false, "italic": false, "underline": false},
     *     "user": {"fg": "208", "bg": "", "bold": false, "italic": false, "underline": false},
     *     "path": {"fg": "124", "bg": "", "bold": false, "italic": false, "underline": false},
     *     "ssh": {"fg": "208", "bg": "52", "bold": false, "italic": false, "underline": false},
     *     "time": {"fg": "124", "bg": "", "bold": false, "italic": true, "underline": false},
     *     "pipenv": {"fg": "#46CC40", "bg": "#24874B", "bold": false, "italic": false, "underline": false},
     *     "dollar": {"fg": "#FF764E", "bg": "#6F2008", "bold": false, "italic": false, "underline": false},
     *   },
     *   "blue": {
     *     "sink": {"fg": "45", "bg": "27", "bold": false, "italic": false, "underline": false},
     *     "virt": {"fg": "blue", "bg": "", "bold": false, "italic": false, "underline": false},
     *     "user": {"fg": "29", "bold": false, "italic": false, "underline": false},
     *     "path": {"fg": "39", "bold": false, "italic": false, "underline": false},
     *     "ssh": {"fg": "green", "bold": false, "italic": false, "underline": false},
     *     "time": {"fg": "39", "bold": false, "italic": false, "underline": false},
     *     "pipenv": {"fg": "#46CC40", "bg": "#24874B", "bold": false, "italic": false, "underline": false},
     *     "dollar": {"fg": "#FF764E", "bg": "#6F2008", "bold": false, "italic": false, "underline": false},
     *   },
     *   "paleblue": {
     *     "sink": {"fg": "#4089CC", "bg": "#23588A", "bold": false, "italic": false, "underline": false},
     *     "virt": {"fg": "blue", "bg": "", "bold": false, "italic": false, "underline": false},
     *     "ssh": {"fg": "208", "bg": "52", "bold": false, "italic": false, "underline": false},
     *     "user": {"fg": "#88B76C", "bold": false, "italic": false, "underline": false},
     *     "path": {"fg": "#5D9FDE", "bold": false, "italic": true, "underline": false},
     *     "time": {"fg": "#5D9FDE", "bold": false, "italic": false, "underline": false},
     *     "pipenv": {"fg": "#46CC40", "bg": "#24874B", "bold": false, "italic": false, "underline": false},
     *     "dollar": {"fg": "#FF764E", "bg": "#6F2008", "bold": false, "italic": false, "underline": false},
     *   }
     * } */
    // var themes_data = JSON.parse('{"red":{"sink":{"fg":"red","bg":"darkred","bold":false,"italic":false,"underline":false},"virt":{"fg":"208","bg":"52","bold":false,"italic":false,"underline":false},"user":{"fg":"208","bg":"","bold":false,"italic":false,"underline":false},"path":{"fg":"124","bg":"","bold":false,"italic":false,"underline":false},"ssh":{"fg":"208","bg":"52","bold":false,"italic":false,"underline":false},"time":{"fg":"124","bg":"","bold":false,"italic":true,"underline":false},"pipenv":{"fg":"#46CC40","bg":"#24874B","bold":false,"italic":false,"underline":false},"dollar":{"fg":"#FF764E","bg":"#6F2008","bold":false,"italic":false,"underline":false}},"blue":{"sink":{"fg":"45","bg":"27","bold":false,"italic":false,"underline":false},"virt":{"fg":"blue","bg":"","bold":false,"italic":false,"underline":false},"user":{"fg":"29","bold":false,"italic":false,"underline":false},"path":{"fg":"39","bold":false,"italic":false,"underline":false},"ssh":{"fg":"green","bold":false,"italic":false,"underline":false},"time":{"fg":"39","bold":false,"italic":false,"underline":false},"pipenv":{"fg":"#46CC40","bg":"#24874B","bold":false,"italic":false,"underline":false},"dollar":{"fg":"#FF764E","bg":"#6F2008","bold":false,"italic":false,"underline":false}},"paleblue":{"sink":{"fg":"#4089CC","bg":"#23588A","bold":false,"italic":false,"underline":false},"virt":{"fg":"blue","bg":"","bold":false,"italic":false,"underline":false},"ssh":{"fg":"208","bg":"52","bold":false,"italic":false,"underline":false},"user":{"fg":"#88B76C","bold":false,"italic":false,"underline":false},"path":{"fg":"#5D9FDE","bold":false,"italic":true,"underline":false},"time":{"fg":"#5D9FDE","bold":false,"italic":false,"underline":false},"pipenv":{"fg":"#46CC40","bg":"#24874B","bold":false,"italic":false,"underline":false},"dollar":{"fg":"#FF764E","bg":"#6F2008","bold":false,"italic":false,"underline":false}}}')
    pywebview.api.get_themes().then(function(r){
      console.log(r)
      window.themes = r.themes
    })
    return {
      themes_data: themes_data
    }
  },
  components: {
    Theme
  },
}
</script>

<style>
body{
  color: #BFBFBF;
  background-color: #1E1E1E;
  font-family: mono;


}
#app {
  /* font-family: 'Avenir', Helvetica, Arial, sans-serif; */
  /* color: blue; */
  /* margin-top: 60px; */
}
</style>
