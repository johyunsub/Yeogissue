<template>
    <v-list color="transparent">
        <v-list-item-title> {{name}} </v-list-item-title>
        <v-list-item
            v-for="n in 5"
            :key="n"
            link
            >
            <v-list-item-content>
                <v-list-item-title>
                    List Item {{ n }}
                </v-list-item-title>
            </v-list-item-content>
        </v-list-item>

    </v-list>
</template>

<script>
export default {
    props :{
        name : { type: String },
    }
}
</script>