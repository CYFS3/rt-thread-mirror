# 厂家 SDK 软件包测试清单

统计口径：

- 主清单统计 `bsp` 下默认配置（`rtconfig.h` 或 `.config`）已启用的厂家 HAL/CMSIS/SDK/Series Driver/WiFi SDK 软件包。
- 统计时按 `PKG_USING_*` 宏去掉版本宏，例如 `_LATEST_VERSION`、`_Vxxx`；通用包如 `CMSIS_CORE`、`mbedtls`、`lwIP`、文件系统、传感器和第三方外设包不计入。
- 本轮重点验证软件包拉取后，厂家 SDK 落在 BSP 上级 `libraries` 目录，并且 BSP 构建脚本、Kconfig、工程生成路径仍能找到对应 SDK。
- 主清单合计：227 个 BSP。补充清单另列默认未启用但 Kconfig 中可选择厂家 SDK 包的 BSP。

## 通用测试项

- [ ] 在目标 BSP 目录执行 `pkgs --update`，确认厂家 SDK 包下载到上级 `libraries`，不是 BSP 本地 `packages`。
- [ ] 执行 `scons --menuconfig`，确认厂家 SDK/HAL/CMSIS/Series Driver 配置项可正常加载。
- [ ] 执行 `scons -c` 后重新 `scons`，确认 `SConstruct`/`SConscript` 能从上级 `libraries` 找到源码、头文件和链接脚本。
- [ ] 执行工程生成命令（如 `scons --target=mdk5`，有对应支持时），确认生成工程里的 include/source 路径不再指向错误位置。
- [ ] 检查发布/打包流程（如对应 BSP 的 `dist` 或 `sdk_dist.py`），确认需要的 `libraries` 内容能被带入发布目录。

## 主清单

### AT32（18）

- [ ] A403A：`AT32A403A_CMSIS_DRIVER`, `AT32A403A_HAL_DRIVER`；BSP：`at32/at32a403a-start`
- [ ] A423：`AT32A423_CMSIS_DRIVER`, `AT32A423_HAL_DRIVER`；BSP：`at32/at32a423-start`
- [ ] F402/405：`AT32F402_405_CMSIS_DRIVER`, `AT32F402_405_HAL_DRIVER`；BSP：`at32/at32f402-start`, `at32/at32f405-start`
- [ ] F403A/407：`AT32F403A_407_CMSIS_DRIVER`, `AT32F403A_407_HAL_DRIVER`；BSP：`at32/at32f403a-start`, `at32/at32f407-start`
- [ ] F413：`AT32F413_CMSIS_DRIVER`, `AT32F413_HAL_DRIVER`；BSP：`at32/at32f413-start`
- [ ] F415：`AT32F415_CMSIS_DRIVER`, `AT32F415_HAL_DRIVER`；BSP：`at32/at32f415-start`
- [ ] F421：`AT32F421_CMSIS_DRIVER`, `AT32F421_HAL_DRIVER`；BSP：`at32/at32f421-start`
- [ ] F423：`AT32F423_CMSIS_DRIVER`, `AT32F423_HAL_DRIVER`；BSP：`at32/at32f423-start`
- [ ] F425：`AT32F425_CMSIS_DRIVER`, `AT32F425_HAL_DRIVER`；BSP：`at32/at32f425-start`
- [ ] F435/437：`AT32F435_437_CMSIS_DRIVER`, `AT32F435_437_HAL_DRIVER`；BSP：`at32/at32f435-start`, `at32/at32f437-start`
- [ ] F45x：`AT32F45x_CMSIS_DRIVER`, `AT32F45x_HAL_DRIVER`；BSP：`at32/at32f455-start`, `at32/at32f456-start`, `at32/at32f457-start`
- [ ] M412/416：`AT32M412_416_CMSIS_DRIVER`, `AT32M412_416_HAL_DRIVER`；BSP：`at32/at32m412-start`, `at32/at32m416-start`

### Bluetrum（1）

- [ ] AB32VG1：`BLUETRUM_SDK`；BSP：`bluetrum/ab32vg1-ab-prougen`

### Bouffalo Lab（1）

- [ ] BL808 M0 WLAN：`WLAN_BL808`；BSP：`bouffalo_lab/bl808/m0`

### ESP32（1）

- [ ] ESP32-C3：`ESP_IDF`；BSP：`ESP32_C3`

### FT32（2）

- [ ] FT32F0：`FT32F0_CMSIS_DRIVER`, `FT32F0_STD_DRIVER`；BSP：`ft32/ft32f072xb-starter`
- [ ] FT32F4：`FT32F4_CMSIS_DRIVER`, `FT32F4_STD_DRIVER`；BSP：`ft32/ft32f407xe-starter`

### GD32（22）

- [ ] GD32 ARM：`GD32_ARM_CMSIS_DRIVER`, `GD32_ARM_SERIES_DRIVER`；BSP：`gd32/arm/gd32103c-eval`, `gd32/arm/gd32105c-eval`, `gd32/arm/gd32105r-start`, `gd32/arm/gd32107c-eval`, `gd32/arm/gd32205r-start`, `gd32/arm/gd32207i-eval`, `gd32/arm/gd32303c-start`, `gd32/arm/gd32303e-eval`, `gd32/arm/gd32305r-start`, `gd32/arm/gd32307e-start`, `gd32/arm/gd32405rg`, `gd32/arm/gd32407v-lckfb`, `gd32/arm/gd32407v-start`, `gd32/arm/gd32450z-eval`, `gd32/arm/gd32470i-eval`, `gd32/arm/gd32470z-lckfb`, `gd32/arm/gd32527I-eval`, `gd32/arm/gd32e230-lckfb`, `gd32/arm/gd32e503v-eval`, `gd32/arm/gd32h759i-eval`, `gd32/arm/gd32h759i-start`
- [ ] GD32 RISC-V/VW55x：`GD32_RISCV_SERIES_DRIVER`, `GD32VW55X_WIFI`；BSP：`gd32/risc-v/gd32vw553h-eval`

### HC32（7）

- [ ] HC32F3：`HC32F3_CMSIS_DRIVER`, `HC32F3_SERIES_DRIVER`；BSP：`hc32/ev_hc32f334_lqfp64`
- [ ] HC32F4：`HC32F4_CMSIS_DRIVER`, `HC32F4_SERIES_DRIVER`；BSP：`hc32/ev_hc32f448_lqfp80`, `hc32/ev_hc32f460_lqfp100_v2`, `hc32/ev_hc32f472_lqfp100`, `hc32/ev_hc32f4a0_lqfp176`, `hc32/ev_hc32f4a8_lqfp176`, `hc32/lckfb-hc32f4a0-lqfp100`

### HPMicro（11）

- [ ] HPM SDK：`HPM_SDK`；BSP：`hpmicro/hpm5300evk`, `hpmicro/hpm5301evklite`, `hpmicro/hpm5e00evk`, `hpmicro/hpm6200evk`, `hpmicro/hpm6300evk`, `hpmicro/hpm6750evk`, `hpmicro/hpm6750evk2`, `hpmicro/hpm6750evkmini`, `hpmicro/hpm6800evk`, `hpmicro/hpm6e00evk`, `hpmicro/hpm6p00evk`

### Infineon（8）

- [ ] PSoC6：`INFINEON_CAPSENSE`, `INFINEON_CAT1CM0P`, `INFINEON_CMSIS`, `INFINEON_CORE_LIB`, `INFINEON_MTB_HAL_CAT1`, `INFINEON_MTB_PDL_CAT1`, `INFINEON_RETARGET_IO`；BSP：`Infineon/psoc6-cy8ckit-062-BLE`, `Infineon/psoc6-cy8ckit-062-WIFI-BT`, `Infineon/psoc6-cy8ckit-062S2-43012`, `Infineon/psoc6-cy8ckit-062s4`, `Infineon/psoc6-cy8cproto-062S3-4343W`, `Infineon/psoc6-evaluationkit-062S2`
- [ ] XMC7000：`INFINEON_CAT1CM0P`, `INFINEON_CMSIS`, `INFINEON_CORE_LIB`, `INFINEON_MTB_HAL_CAT1`, `INFINEON_MTB_PDL_CAT1`, `INFINEON_RETARGET_IO`；BSP：`Infineon/xmc7100d-f144k4160aa`, `Infineon/xmc7200-kit_xmc7200_evk`

### Kendryte（1）

- [ ] K210：`K210_SDK`；BSP：`k210`

### MM32（1）

- [ ] MM32：`MM32`；BSP：`mm32f526x`

### Nuclei（2）

- [ ] Nuclei SDK：`NUCLEI_SDK`；BSP：`nuclei/gd32vf103_rvstar`, `nuclei/nuclei_fpga_eval`

### Nuvoton（12）

- [ ] Nuvoton Series Driver：`NUVOTON_SERIES_DRIVER`；BSP：`nuvoton/ma35-rtp`, `nuvoton/nk-980iot`, `nuvoton/nk-n9h30`, `nuvoton/nk-rtu980`, `nuvoton/numaker-hmi-ma35d1`, `nuvoton/numaker-iot-m467`, `nuvoton/numaker-iot-m487`, `nuvoton/numaker-iot-ma35d1`, `nuvoton/numaker-m032ki`, `nuvoton/numaker-m2354`, `nuvoton/numaker-m467hj`, `nuvoton/numaker-pfm-m487`

### NXP（32）

- [ ] i.MX6SX：`NXP_IMX6SX_DRIVER`；BSP：`nxp/imx/imx6sx/cortex-a9`
- [ ] i.MX6UL/ULL：`NXP_IMX6UL_DRIVER`；BSP：`nxp/imx/imx6ul`, `nxp/imx/imx6ull-smart`
- [ ] i.MXRT：`NXP_IMXRT_DRIVER`；BSP：`nxp/imx/imxrt/imxrt1021-nxp-evk`, `nxp/imx/imxrt/imxrt1052-atk-commander`, `nxp/imx/imxrt/imxrt1052-fire-pro`, `nxp/imx/imxrt/imxrt1052-nxp-evk`, `nxp/imx/imxrt/imxrt1052-seeed-ArchMix`, `nxp/imx/imxrt/imxrt1060-nxp-evk`, `nxp/imx/imxrt/imxrt1061-forlinx-OK1061-S`, `nxp/imx/imxrt/imxrt1064-nxp-evk`, `nxp/imx/imxrt/imxrt1170-nxp-evk`
- [ ] LPC：`NXP_LPC_DRIVER`；BSP：`nxp/lpc/lpc176x`, `nxp/lpc/lpc178x`, `nxp/lpc/lpc408x`, `nxp/lpc/lpc5410x`, `nxp/lpc/lpc54114-lite`, `nxp/lpc/lpc54608-LPCXpresso`, `nxp/lpc/lpc824`
- [ ] LPC55S：`NXP_LPC55S_DRIVER`；BSP：`nxp/lpc/lpc55sxx/lpc55s06_nxp_evk`, `nxp/lpc/lpc55sxx/lpc55s16_nxp_evk`, `nxp/lpc/lpc55sxx/lpc55s28_nxp_evk`, `nxp/lpc/lpc55sxx/lpc55s36_nxp_evk`, `nxp/lpc/lpc55sxx/lpc55s69_nxp_evk`
- [ ] MCX：`NXP_MCX_CMSIS_DRIVER`, `NXP_MCX_SERIES_DRIVER`；BSP：`nxp/mcx/mcxa/frdm-mcxa153`, `nxp/mcx/mcxa/frdm-mcxa156`, `nxp/mcx/mcxa/frdm-mcxa346`, `nxp/mcx/mcxa/frdm-mcxa366`, `nxp/mcx/mcxc/frdm-mcxc444`, `nxp/mcx/mcxe/frdm-mcxe247`, `nxp/mcx/mcxn/frdm-mcxn236`, `nxp/mcx/mcxn/frdm-mcxn947`

### Raspberry Pi Pico（2）

- [ ] RP2040：`RASPBERRYPI_PICO_SDK`；BSP：`raspberry-pico/RP2040`
- [ ] RP2350：`RASPBERRYPI_PICO_RP2350_SDK`；BSP：`raspberry-pico/RP2350`

### Realtek（1）

- [ ] Ameba：`REALTEK_AMEBA`；BSP：`amebaz`

### STM32（101）

- [ ] STM32F0：`STM32F0_CMSIS_DRIVER`, `STM32F0_HAL_DRIVER`；BSP：`stm32/stm32f072-st-nucleo`, `stm32/stm32f091-st-nucleo`
- [ ] STM32F1：`STM32F1_CMSIS_DRIVER`, `STM32F1_HAL_DRIVER`；BSP：`stm32/stm32f103-100ask-mini`, `stm32/stm32f103-100ask-pro`, `stm32/stm32f103-atk-nano`, `stm32/stm32f103-atk-warshipv3`, `stm32/stm32f103-blue-pill`, `stm32/stm32f103-dofly-lyc8`, `stm32/stm32f103-dofly-M3S`, `stm32/stm32f103-fire-arbitrary`, `stm32/stm32f103-gizwits-gokitv21`, `stm32/stm32f103-hw100k-ibox`, `stm32/stm32f103-keysking-learning`, `stm32/stm32f103-onenet-nbiot`, `stm32/stm32f103-yf-ufun`, `stm32/stm32f103-ys-f1pro`, `stm32/stm32f107-uc-eval`
- [ ] STM32F2：`STM32F2_CMSIS_DRIVER`, `STM32F2_HAL_DRIVER`；BSP：`stm32/stm32f207-st-nucleo`
- [ ] STM32F3：`STM32F3_CMSIS_DRIVER`, `STM32F3_HAL_DRIVER`；BSP：`stm32/stm32f302-st-nucleo`, `stm32/stm32f334-st-nucleo`
- [ ] STM32F4：`STM32F4_CMSIS_DRIVER`, `STM32F4_HAL_DRIVER`；BSP：`stm32/stm32f401-st-nucleo`, `stm32/stm32f401-weact-blackpill`, `stm32/stm32f405-smdz-breadfruit`, `stm32/stm32f405zg-mini-template`, `stm32/stm32f407-armfly-v5`, `stm32/stm32f407-atk-explorer`, `stm32/stm32f407-fk407m2-zgt6`, `stm32/stm32f407-lckfb-skystar`, `stm32/stm32f407-micu`, `stm32/stm32f407-robomaster-c`, `stm32/stm32f407-rt-spark`, `stm32/stm32f407-st-discovery`, `stm32/stm32f410-st-nucleo`, `stm32/stm32f411-atk-nano`, `stm32/stm32f411-st-nucleo`, `stm32/stm32f411-weact-blackpill`, `stm32/stm32f412-st-nucleo`, `stm32/stm32f413-st-nucleo`, `stm32/stm32f427-robomaster-a`, `stm32/stm32f429-armfly-v6`, `stm32/stm32f429-atk-apollo`, `stm32/stm32f429-fire-challenger`, `stm32/stm32f429-st-disco`, `stm32/stm32f446-st-nucleo`, `stm32/stm32f469-st-disco`
- [ ] STM32F7：`STM32F7_CMSIS_DRIVER`, `STM32F7_HAL_DRIVER`；BSP：`stm32/stm32f723-st-disco`, `stm32/stm32f746-st-disco`, `stm32/stm32f746-st-nucleo`, `stm32/stm32f767-atk-apollo`, `stm32/stm32f767-fire-challenger-v1`, `stm32/stm32f767-st-nucleo`, `stm32/stm32f769-st-disco`
- [ ] STM32G0：`STM32G0_CMSIS_DRIVER`, `STM32G0_HAL_DRIVER`；BSP：`stm32/stm32g030-tiny-board`, `stm32/stm32g070-st-nucleo`, `stm32/stm32g071-st-nucleo`
- [ ] STM32G4：`STM32G4_CMSIS_DRIVER`, `STM32G4_HAL_DRIVER`；BSP：`stm32/stm32g431-st-nucleo`, `stm32/stm32g474-st-nucleo`, `stm32/stm32g491-st-nucleo`
- [ ] STM32H5：`STM32H5_CMSIS_DRIVER`, `STM32H5_HAL_DRIVER`；BSP：`stm32/stm32h503-st-nucleo`, `stm32/stm32h563-st-nucleo`
- [ ] STM32H7：`STM32H7_CMSIS_DRIVER`, `STM32H7_HAL_DRIVER`；BSP：`stm32/stm32h723-lxb-disco`, `stm32/stm32h723-st-nucleo`, `stm32/stm32h730-esphosted-evb`, `stm32/stm32h743-armfly-v7`, `stm32/stm32h743-atk-apollo`, `stm32/stm32h743-openmv-h7plus`, `stm32/stm32h743-st-nucleo`, `stm32/stm32h747-st-discovery`, `stm32/stm32h750-armfly-h7-tool`, `stm32/stm32h750-artpi`, `stm32/stm32h750-fk750m1-vbt6`, `stm32/stm32h750-weact-ministm32h7xx`
- [ ] STM32H7RS：`STM32H7RS_CMSIS_DRIVER`, `STM32H7RS_HAL_DRIVER`；BSP：`stm32/stm32h7r7-artpi2`, `stm32/stm32h7s7-st-disco`
- [ ] STM32L0：`STM32L0_CMSIS_DRIVER`, `STM32L0_HAL_DRIVER`；BSP：`stm32/stm32l010-st-nucleo`, `stm32/stm32l053-st-nucleo`
- [ ] STM32L4：`STM32L4_CMSIS_DRIVER`, `STM32L4_HAL_DRIVER`；BSP：`stm32/stm32l412-st-nucleo`, `stm32/stm32l431-BearPi`, `stm32/stm32l431-tencentos-tiny-EVB_MX+`, `stm32/stm32l432-st-nucleo`, `stm32/stm32l433-ali-startkit`, `stm32/stm32l433-st-nucleo`, `stm32/stm32l452-st-nucleo`, `stm32/stm32l475-atk-pandora`, `stm32/stm32l475-st-discovery`, `stm32/stm32l476-st-nucleo`, `stm32/stm32l496-ali-developer`, `stm32/stm32l496-st-discovery`, `stm32/stm32l496-st-nucleo`, `stm32/stm32l4r5-st-nucleo`, `stm32/stm32l4r9-st-eval`, `stm32/stm32l4r9-st-sensortile-box`
- [ ] STM32L5：`STM32L5_CMSIS_DRIVER`, `STM32L5_HAL_DRIVER`；BSP：`stm32/stm32l552-st-nucleo`
- [ ] STM32MP1：`STM32MP1_M4_CMSIS_DRIVER`, `STM32MP1_M4_HAL_DRIVER`；BSP：`stm32/stm32mp157a-st-discovery`, `stm32/stm32mp157a-st-ev1`
- [ ] STM32U5：`STM32U5_CMSIS_DRIVER`, `STM32U5_HAL_DRIVER`；BSP：`stm32/stm32u575-st-nucleo`, `stm32/stm32u585-iot02a`
- [ ] STM32WB：`STM32WB_CMSIS_DRIVER`, `STM32WB_HAL_DRIVER`；BSP：`stm32/stm32wb55-st-nucleo`
- [ ] STM32WL：`STM32WL_CMSIS_DRIVER`, `STM32WL_HAL_DRIVER`；BSP：`stm32/stm32wl55-st-nucleo`, `stm32/stm32wle5-yizhilian-lm401`, `stm32/stm32wle5-yizhilian-lm402`

### WCH（3）

- [ ] CH32V20x：`CH32V20x_SDK`；BSP：`wch/risc-v/ch32v208w-r0`
- [ ] CH32V307：`CH32V307_SDK`；BSP：`wch/risc-v/ch32v307v-r1`, `wch/risc-v/yd-ch32v307vct6`

### WinnerMicro（1）

- [ ] W60x：`WM_LIBRARIES`；BSP：`w60x`

## 补充清单：Kconfig 条件启用项

这些 BSP 默认配置未启用对应厂家 SDK 包，但板级 Kconfig 中存在条件选择；如本次测试覆盖可选驱动，也需要点选后验证。

- [ ] nRF5x SoftDevice：`NRF5X_SDK`，选择 `BSP_USING_SOFTDEVICE` 后启用；BSP：`nrf5x/nrf52832`, `nrf5x/nrf52833`, `nrf5x/nrf52840`
