[![HACS Default][hacs_shield]][hacs]
[![GitHub Latest Release][releases_shield]][latest_release]
[![GitHub All Releases][downloads_total_shield]][releases]
[![Buy me a coffee][buy_me_a_coffee_shield]][buy_me_a_coffee]
[![PayPal.Me][paypal_me_shield]][paypal_me]

[hacs_shield]: https://img.shields.io/static/v1.svg?label=HACS&message=Custom&style=for-the-badge&color=green&labelColor=41bdf5&logo=HomeAssistantCommunityStore&logoColor=white
[hacs]: https://hacs.xyz/
[latest_release]: https://github.com/clementprevot/aduro/releases/latest
[releases_shield]: https://img.shields.io/github/release/clementprevot/aduro.svg?style=for-the-badge
[releases]: https://github.com/clementprevot/aduro/releases
[downloads_total_shield]: https://img.shields.io/github/downloads/clementprevot/aduro/total?style=for-the-badge
[buy_me_a_coffee_shield]: https://img.shields.io/static/v1.svg?label=%20&message=Buy%20me%20a%20pizza&color=ff6937&logo=buy%20me%20a%20coffee&style=for-the-badge&logoColor=white
[buy_me_a_coffee]: https://www.buymeacoffee.com/clementprevot
[paypal_me_shield]: https://img.shields.io/static/v1.svg?label=%20&message=PayPal.Me&style=for-the-badge&logo=paypal
[paypal_me]: https://paypal.me/clementprevot

# Aduro

This custom integration provides support for Aduro burners such Aduro H1 & H2.

> Note that this integration may also work for any NBE compatible burner/boiler.
> For more information about NBE, please refer to
> [this repository](https://github.com/motoz/nbetest) and
> [this library](https://github.com/clementprevot/pyduro).

## Installation

### Using HACS (recommended)

This integration can be installed using [HACS](https://hacs.xyz/).

To do it search for `Aduro` in _Integrations_ section.

### Manual

To install this integration manually you have to clone this repository (or
download it as a zip) and copy/extract it to
`config/custom_components/aduro` directory:

```bash
mkdir -p custom_components/aduro
cd custom_components/aduro
wget https://github.com/clementprevot/aduro/archive/refs/heads/main.zip
unzip main.zip
rm main.zip
```

## Configuration

TBD
