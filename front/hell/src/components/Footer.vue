<template>
  <div class="mt-10 mb-5 text-center">
    © 2021, made with by DongKyu Company for a better web.

    <div class="pt-2">
      후원문의 : 카카오뱅크 3333-07-9600044 강구원
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    movepage() {
      this.$router.push(`/TeamIntro`);
    },
  },
};
</script>
