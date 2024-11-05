plugins {
    application
}

group = "hse"
version = "1.0-SNAPSHOT"

application {
    mainClass.set("hse.Main")
}

repositories {
    mavenCentral()
}

dependencies {
    testImplementation(platform("org.junit:junit-bom:5.10.0"))
    testImplementation("org.junit.jupiter:junit-jupiter")
}

tasks.test {
    useJUnitPlatform()
}