import os
import re


raag_list = "1. Asa 2. Gujari 3. Gauri Deepaki 4. Dhanasri 5. Gauri Poorabi 6. Siri 7. Majh 8. Gauri Guarairee 9. Gauri 10. Gauri Dakhani 11. Gauri Chaitee 12. Gauri Bairagan 13. Gauri Poorabi Deepaki 14. Gauri Malva 15. Gauri Mala 16. Gauri Majh 17. Gauri Sorath 18. Asa Kafi 19. Asavari 20. Asa Asavari 21. Devgandhari 22. Bihagra 23. Vadhans 24. Vadhans Dakhani 25. Sorath 26. Jaitsri 27. Todi 28. Bairarri 29. Tilang 30. Tilang Kafi 31. Suhee 32. Suhee Kafi 33. Suhee Lalit 34. Bilaval 35. Bilaval Dakhani 36. Gound 37. Bilaval Gound 38. Ramkali 39. Ramkali Dakhani 40. Nut Narayan 41. Nut 42. Mali Gaura 43. Maru 44. Maru Kafi 45. Maru Dakhani 46. Tukhari 47. Kedara 48. Bhairo 49. Basant 50. Basant Hindol 51. Sarang 52. Malhar 53. Kanra 54. Kaliyan 55. Kaliyan Bhopali 56. Parbhati 57. Parbhati Bibhas 58. Bibhas Parbhati 59. Parbhati Dakhani 60. Jaijavanti"
rl = re.sub(r'\d+', '', raag_list)

rl_2 = rl.split(' . ')

for i in rl_2:
    os.mkdir(i)