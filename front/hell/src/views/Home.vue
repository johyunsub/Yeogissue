<template>
  <v-row class="justify-center">
    <div class="home-image">
      <div class="ma-auto mt-10" style="width: 40%; height:100px">
        <VueSlickCarousel v-bind="slickOptions" :style="{ height: '100px' }">
          <div><img :src="require('../assets/의견 이슈.png')" style="height:100px; width:100px;" alt="" /></div>
          <div><img :src="require('../assets/모여 이슈.png')" style="height:100px; width:100px;" alt="" /></div>
          <div><img :src="require('../assets/매거진메인.png')" style="height:100px; width:100px;" alt="" /></div>
          <div><img :src="require('../assets/이슈메인.png')" style="height:100px; width:100px;" alt="" /></div>
        </VueSlickCarousel>
      </div>
    </div>
  </v-row>
</template>

<script>
import VueSlickCarousel from "vue-slick-carousel";
import "vue-slick-carousel/dist/vue-slick-carousel.css";
import "vue-slick-carousel/dist/vue-slick-carousel-theme.css";

export default {
  name: "Home",
  components: { VueSlickCarousel },
  data: () => ({
    slickOptions: {
      slidesToShow: 1,
      slidesToScroll: 1,
      speed: 400,
      autoplay: true,
      arrows: false,
      autoplaySpeed: 1500,
      vertical: true,
      verticalSwiping: true,
    },
    items: {},
  }),
};
</script>

<style>
.home-image {
  width: 100%;
  height: 800px;
  background-color: #5e35b1;
  background-size: 100% 600px;
}

.opinion-image {
  width: 100%;
  height: 800px;
  background-color: #5e35b1;
  background-size: 100% 600px;
}

.club-image {
  width: 100%;
  height: 800px;
  background-color: #5e35b1;
  background-size: 100% 600px;
}

.-image {
  width: 100%;
  height: 800px;
  background-color: #5e35b1;
  background-size: 100% 600px;
}

.home-image {
  width: 100%;
  height: 800px;
  background-color: #5e35b1;
  background-size: 100% 600px;
}
</style>
