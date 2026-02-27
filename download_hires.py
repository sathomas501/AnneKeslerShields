import os
import urllib.request
import time

dest = 'C:/Users/Owner/OneDrive/Documents/GitHub/annekeslershields/images'

# All images used in the galleries
images = [
    # op art
    "7eba9c_720a655aa51e4730a021f7593b1518b0_mv2.jpg",
    "7eba9c_cbf543382edb468391983bd009a8668b_mv2.jpg",
    "7eba9c_a50b35e701bc42a09bc835b9aa29366e_mv2.jpg",
    "7eba9c_1800e664b3684fc0a4e36b36941ae719_mv2.jpg",
    "7eba9c_cc44a78e3d1c43a49a5006c1056596de_mv2.jpg",
    "7eba9c_16ee5afbfcef452bbbf0f9e4c1226fa8_mv2.jpg",
    "7eba9c_a555406826e74c52a9d17c36b1da5c8b_mv2.jpg",
    "7eba9c_b59716abe3ee43d9b09d470455be7128_mv2.jpg",
    "7eba9c_1c8e0325b217448d91e0ca8604f713a3_mv2.jpg",
    "7eba9c_1994f379811548539273b4c03c7bc598_mv2.jpg",
    "7eba9c_7a41c85ba34f4191b8f141935fc7cfd0_mv2.jpg",
    "7eba9c_137b0d53101e48988d11fa48798a4604_mv2.jpg",
    "7eba9c_527e6c12fcdf4b2baa4c8174e0896180_mv2.jpg",
    "7eba9c_182617dc8e354dcd924b62ab7babe84c_mv2.jpg",
    "7eba9c_6ebe4b42eedd4e66ac8e2a140402046f_mv2.jpg",
    "7eba9c_00ddad8e2b494126ac4e52a664f8d2ac_mv2.jpg",
    "7eba9c_05a6838ddabe4474a6f7784663128df7_mv2.jpg",
    "7eba9c_e409a2328af54ce998c2ff280420c6f3_mv2.jpg",
    "7eba9c_62f1204a09aa48348d43ce9558b2e764_mv2.jpg",
    "7eba9c_080ad6c9c7554498ae8c27e4a56ba85f_mv2.jpg",
    "7eba9c_8b3ce335344b4deea72430024a04ece8_mv2.jpg",
    "7eba9c_8902ce35309a4f9d9d49d6c861c444a8_mv2.jpg",
    "7eba9c_44b39f9fcdff4f4b939bce12f74890d5_mv2.jpg",
    "7eba9c_493b1055892e44139fee4ce5b2c23ab4_mv2.jpg",
    "7eba9c_6234455ef0a945e7820fc6e8a52f5f32_mv2.jpg",
    "7eba9c_0eeceab5acf44711a4dd0caa0075aaea_mv2.jpg",
    # oil paintings
    "7eba9c_b06b9c9cc0ba44cea56ba5eae881c958_mv2.jpg",
    "7eba9c_a9d84835f6cc47cb9c05e1ea3b8c2e89_mv2.jpg",
    "7eba9c_0b1f97c5e70a49b99675e0c12cd1ca42_mv2.jpg",
    "7eba9c_6ac5434dde064815b1b206be3e3784c6_mv2.jpg",
    "7eba9c_beb95d9b340f48bdab5b2191186f400b_mv2.jpg",
    "7eba9c_e400ec5b0ae94bb5aa5f7cd477836c31_mv2.jpg",
    "7eba9c_30e4ba4d80cf4ca8a219fb795e5a4b7b_mv2.jpg",
    # woodcuts
    "7eba9c_3ed1ca149ca845f3b866cd460b3411ea_mv2.jpg",
    "7eba9c_29ac87bae964434ebadbd652f9af7f05_mv2.jpg",
    "7eba9c_e3b0e1d4c6e049738e93c7de75a29f81_mv2.jpg",
    "7eba9c_ea393f251f304144b6ac82ef76c7facc_mv2.jpg",
    "7eba9c_c4eea9b9077f41dcb961d99880115bbd_mv2.jpg",
    "7eba9c_eaf3f850d6004059a65d908495fbca15_mv2.jpg",
    # portraiture
    "7eba9c_0eb6eae56471470485972fde066b73c4_mv2.jpg",
    "7eba9c_f15a0907ba0f41b296a7763c8634cb74_mv2.jpg",
    "7eba9c_fa754a7978134e1b8560091a652c80b2_mv2.jpg",
    "7eba9c_befde8a7aa224d8ba983e6605926047c_mv2.jpg",
    "7eba9c_51ba9807ae91402fb4dd7e6771ecc543_mv2.jpg",
    "7eba9c_fee98538bdda44db998ea763f011425e_mv2.jpg",
    "7eba9c_00f331d49564406bab2f96e9dcffed1f_mv2.jpg",
    "7eba9c_f6a93853fc6c47cab084f4fe9565ffc7_mv2.jpg",
    "7eba9c_32194a63f5434b688019c35e5cc62ec5_mv2.jpg",
    "7eba9c_a7583db24f5c444c96bd78c4f7cddc20_mv2.jpg",
    "7eba9c_96b163b49d114a2bbdd7c99c21768660_mv2.jpg",
    # appropriated images
    "7eba9c_5443eb548b374014b16cba0bee231f7a_mv2.jpg",
    "7eba9c_0a67c2f498d74acb9951144ba0383aee_mv2.jpg",
    "7eba9c_2840774252d3418ba73abbee0c4c0fdb_mv2.jpeg",
    "7eba9c_2dfbdba0a56d444aaaacdc836c434c8c_mv2.jpeg",
    "7eba9c_7d5143929410448ba512d6af4bcfbcb7_mv2.jpg",
    "7eba9c_b4f68c3eb7f945edb7fadb706f9260d1_mv2.jpeg",
    "7eba9c_c9e137d62bdf4cdea74b60f9ba22f167_mv2.jpeg",
    "7eba9c_ea66de1480994d77b62b92b5de3070c1_mv2.jpeg",
    "7eba9c_03d6d1d437f24b57ab0ed27728beffb5_mv2.jpeg",
    "7eba9c_e65d7cb32cbe45529ffaf7d306d7969c_mv2.jpg",
    "7eba9c_284e0628762d4ba286097ff4afd61ab4_mv2.jpg",
    "7eba9c_44573fc779e648afb22390a0eec087af_mv2.jpeg",
    "7eba9c_e738310054eb4c52960d924841ad0678_mv2.jpg",
    "7eba9c_36120619c1974fc1badbfa9652f0243e_mv2.jpeg",
    "7eba9c_df09c039174644808607246a634d3f73_mv2.jpg",
    "7eba9c_05108f1db41646f0b02b23e35da8fb53_mv2.jpg",
    "7eba9c_4b11272ca8c1432da9cd3dcf5d785a99_mv2.jpg",
    "7eba9c_7b1718ad1a8043faaaae782913de8d73_mv2.jpg",
    "7eba9c_dffc27a91cb34734abb2bfe4f04fec4b_mv2.jpg",
    "7eba9c_42436a06472b4f55b7140d4352d8426e_mv2.jpg",
    "7eba9c_907ef2b472154252b3f5c2877db5a050_mv2.jpeg",
    "7eba9c_d3ecf9e389524a489060dbc94e5765f0_mv2.jpeg",
    "7eba9c_d480180102da4836bb4f3a854434c775_mv2.jpg",
    "7eba9c_1680a3f5b94e4c46b054b32754a8aee9_mv2.jpeg",
    "7eba9c_cc6ffda2b80946919a9328e7c9fce71a_mv2.jpeg",
    "7eba9c_422823cf4ead47b88ffdf4fe02540d49_mv2.jpeg",
    # installations
    "7eba9c_49c4904067514c7d9c619a29ee550e41_mv2.jpg",
    "7eba9c_b3686cd823cc48fd95baa06feb2f1c49_mv2.jpg",
    "7eba9c_d4be1708e7c94a188cd7e6f741b965bd_mv2.jpg",
    "7eba9c_6662ad92e5f04d75bcc40e73568bd9a4_mv2.jpg",
    "7eba9c_558435ee9dc84e3a84da476cd1f3b8e4_mv2.jpg",
    "7eba9c_89203b2697954996aca3e4d30b7552d2_mv2.jpg",
    "7eba9c_2df3a5ada706456fac2e3e5b730918e9_mv2.jpg",
    "7eba9c_e75337be208149aeb7762a7955760117_mv2.jpg",
    "7eba9c_fa8d3c2811bb46869ca293b873427932_mv2.jpg",
    "7eba9c_1b8d2f98217c4e05a16972fa28d944d0_mv2.jpg",
    "7eba9c_16608719f3c8419bb21e8fa37a750dfb_mv2.jpg",
    "7eba9c_07b65132c06c46e5a3c3bf0afcf16d5d_mv2.jpg",
    "7eba9c_89607439864f4e4fab846daa4976d03d_mv2.jpg",
    "7eba9c_c84613f5caee419eaf444bcd9cbc8536_mv2.jpg",
    # sculpture
    "7eba9c_10d2fc646bb5472ea101427314dc8e1c_mv2.jpg",
    "7eba9c_450a9979df5a4228be0a8a145bf8c2fa_mv2.jpg",
    "7eba9c_ccbe36a55fe4439db17a588f4d9e94a3_mv2.jpg",
    "7eba9c_c30acd08760040509202523e82863fcc_mv2.jpg",
    # secca
    "7eba9c_8bd19cccdd5b4bceb879d04fce49c003_mv2.jpg",
    "7eba9c_035f2f6188104992bfb99c87a708dd72_mv2.jpg",
    "7eba9c_fc833840c2ee43458a06d01889c14713_mv2.jpg",
    "7eba9c_33733285f7084cfbb0b9771de5159e63_mv2.jpg",
    "7eba9c_f8b846f5e09b4a7d8a61363400b21769_mv2.jpg",
    "7eba9c_108c598089394319b513f2858d995a05_mv2.jpg",
    "7eba9c_b167e952642c4b9a8aef3c61036e3efd_mv2.jpg",
    "7eba9c_0af794591b594fe0b38300f0a2b76187_mv2.jpg",
    "7eba9c_19336f45fd1548dc982208709bc1f8fd_mv2.jpg",
    "7eba9c_8d951638aadb46e5abb006993e38cca5_mv2.jpg",
    "7eba9c_567706cf36d2426bac8662a363e28183_mv2.jpg",
    "7eba9c_28b3dfc5d4094842ac84ce25870e0830_mv2.jpg",
    "7eba9c_4b93838fbe154b9e91edde245e522716_mv2.jpg",
    "7eba9c_aeb42414036f4cc1ae76ce7ff7199c29_mv2.jpg",
    "7eba9c_32d0194e48ee4bc884b7bbf020d687b3_mv2.jpg",
    "7eba9c_e1633d318c2446b28fb9bdfe8c9e35c4_mv2.jpg",
    "7eba9c_b8d0a3cddddf4f85afa9c2d98f9957b7_mv2.jpg",
    "7eba9c_5cfd6d89a2b1489e9b1bb22895498364_mv2.jpg",
    "7eba9c_c9560d4e919342b4a20f84ee9cf148f6_mv2.jpg",
    "7eba9c_01ea9cba9e15429aa3ff9e2c697bb57a_mv2.jpg",
    "7eba9c_fa6bc288a8df419cb021eacc1f1419ba_mv2.jpg",
    "7eba9c_18257214566d42888309edf3f49a495e_mv2.jpg",
    "7eba9c_3965834063614911b56c2a9f2eb994e4_mv2.jpg",
    "7eba9c_9298deba6a0840c5b9bb7c08d23967cb_mv2.jpg",
    # arbor acres
    "7eba9c_e6ba2c54635c46f3a2c201fdeb8b80f8_mv2.jpg",
    "7eba9c_15bcc53fc0b74741bf117a45d624ee67_mv2.jpg",
    "7eba9c_60e8a4b9b50443658fd10c6a24e36523_mv2.jpg",
    "7eba9c_4a279eacfc624060872a5db5691579de_mv2.jpg",
    "7eba9c_24ed48a242f84505b82ec94e1bbbf1fc_mv2.jpg",
    "7eba9c_b3ed09f4d1d34a2182bf7f5aec2890c4_mv2.jpg",
    "7eba9c_4edcee69ebfa4851bbb618914ec4c7ba_mv2.jpg",
    "7eba9c_dc5f0cfa88074e858c53450bb7ff0504_mv2.jpg",
    "7eba9c_7f04a169aca643789dbde466df02b338_mv2.jpg",
    "7eba9c_8d626e985ce141678f752e6424406c13_mv2.jpg",
    "7eba9c_e147565c0bcb459188369ba8917153c3_mv2.jpg",
    "7eba9c_884194264d40449d905c1d0850a0c122_mv2.jpg",
    "7eba9c_3caab56c128e42dca123b8af8e150c10_mv2.jpg",
    "7eba9c_b0d7ac3b08364dcaae11ba0770c3c3a5_mv2.jpg",
    "7eba9c_61274e9b7b6c4ebbbbf38fb8a383ab3f_mv2.jpg",
    "7eba9c_caafeac3bff340578f7188288ef3acc3_mv2.jpg",
    "7eba9c_8e38da5ed8ac482ebd5842a5f2f9351e_mv2.jpg",
    "7eba9c_21dfe533295e4640928bd50de3c079d5_mv2.jpg",
    "7eba9c_646e8e5d9e054f00bd5869a6cc38fe57_mv2.jpg",
    "7eba9c_ab4d36e3468640a489add4d4e0582e46_mv2.jpg",
    "7eba9c_384bccfdd10549f7a143edcd1dfa6d64_mv2.jpg",
    "7eba9c_71c364300b6b4e679608fa2566138538_mv2.jpg",
    "7eba9c_5e3570554f1c410a9332c5d8a41eb49c_mv2.jpg",
    "7eba9c_41f90290a909469eab38e2e1e411b632_mv2.jpg",
    "7eba9c_87cf7eba00a54ad28b9bdc09a44f8c4c_mv2.jpg",
    "7eba9c_14e7bd22778940dcb7762eb5c39bde88_mv2.jpg",
]

# Deduplicate
images = list(dict.fromkeys(images))

headers = {'User-Agent': 'Mozilla/5.0'}
ok = 0
fail = 0

for fname in images:
    url = f"https://static.wixstatic.com/media/{fname}"
    target = os.path.join(dest, fname)
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read()
        with open(target, 'wb') as f:
            f.write(data)
        size_kb = len(data) // 1024
        print(f"OK  {fname}  ({size_kb} KB)")
        ok += 1
        time.sleep(0.1)  # polite delay
    except Exception as e:
        print(f"FAIL {fname}: {e}")
        fail += 1

print(f"\nDone: {ok} downloaded, {fail} failed")
