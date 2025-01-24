/**
 * Copyright (c) 2024 Piyawish Piyawat
 * Licensed under the MIT License
 */

/*! `piyathon` grammar for highlight.js */
(function () {
  function piyathonLanguage(hljs) {
    console.log("Defining Piyathon language...");
    return {
      name: "Piyathon",
      aliases: ["piyathon", "pi"],
      case_insensitive: false,
      keywords: {
        $pattern: /[ก-๛a-zA-Z_][ก-๛a-zA-Z0-9_]*/,
        keyword:
          "และ เป็น ยืนยัน ไม่ประสาน รอประสาน หยุด เมื่อ ชั้น " +
          "ทำต่อ นิยาม ลบ อื่นถ้า อื่น ยกเว้น สุดท้าย สำหรับ " +
          "จาก ทั่วไป ถ้า นำเข้า ใน คือ แลมบ์ดา เทียบ นอกเขต " +
          "ไม่ หรือ ผ่าน ยก คืนค่า ลอง ขณะ ด้วย ให้",
        built_in:
          "พิมพ์ ช่วง ผลรวม ค่าสูงสุด ค่าต่ำสุด ความยาว " +
          "ค่าสัมบูรณ์ อิเทอเรเตอร์อะซิงค์ ทั้งหมด ถัดไปอะซิงค์ ใดๆ " +
          "แอสกี ฐานสอง บูลีน จุดพัก แถวไบต์ ไบต์ เรียกได้ " +
          "อักขระ เมธอดคลาส คอมไพล์ จำนวนเชิงซ้อน ลบแอททริบิวต์ " +
          "พจนานุกรม ไดเรกทอรี หารเอาเศษ ลำดับ ประเมิน ประมวลผล " +
          "กรอง ทศนิยม จัดรูปแบบ เซ็ตแช่แข็ง รับแอททริบิวต์ " +
          "ตัวแปรโกลบอล มีแอททริบิวต์ แฮช ช่วยเหลือ ฐานสิบหก รหัส " +
          "รับค่า จำนวนเต็ม เป็นอินสแตนซ์ เป็นคลาสลูก วนซ้ำ รายการ " +
          "ตัวแปรท้องถิ่น แปลง มุมมองหน่วยความจำ ถัดไป วัตถุ ฐานแปด " +
          "เปิด รหัสอักขระ ยกกำลัง คุณสมบัติ ตัวแทน ย้อนกลับ " +
          "ปัดเศษ เซ็ต ตั้งแอททริบิวต์ ตัดส่วน เรียงลำดับ เมธอดคงที่ " +
          "สตริง คลาสแม่ ทูเพิล ชนิด ตัวแปร จับคู่",
        literal:
          "จริง เท็จ ไม่มีค่า " +
          "__นำเข้า__ __ชื่อ__ __เอกสาร__ __ไฟล์__ __พจนานุกรม__ " +
          "__แพ็กเกจ__ __เส้นทาง__ __โมดูล__ __คลาสฐาน__ __คลาส__ " +
          "__เริ่มต้น__ __ลบ__ __ตัวแทนทางการ__ __ตัวแทน__ __ไบต์__ " +
          "__จัดรูปแบบ__ __น้อยกว่า__ __น้อยกว่าเท่ากับ__ __เท่ากับ__ " +
          "__ไม่เท่ากับ__ __มากกว่า__ __มากกว่าเท่ากับ__ __แฮช__ __บูลีน__ " +
          "__เรียกใช้__ __ความยาว__ __เข้าถึงสมาชิก__ __กำหนดสมาชิก__ " +
          "__ลบสมาชิก__ __วนซ้ำ__ __ถัดไป__ __เข้า__ __ออก__ " +
          "__ช่องเก็บ__ __ทั้งหมด__",
      },
      contains: [
        hljs.HASH_COMMENT_MODE,
        hljs.NUMBER_MODE,
        {
          className: "string",
          contains: [hljs.BACKSLASH_ESCAPE],
          variants: [
            { begin: /'''/, end: /'''/, relevance: 10 },
            { begin: /"""/, end: /"""/, relevance: 10 },
            { begin: /'/, end: /'/, relevance: 0 },
            { begin: /"/, end: /"/, relevance: 0 },
          ],
        },
        {
          className: "function",
          begin: /\bนิยาม\b/,
          end: ":",
          keywords: "นิยาม",
          contains: [
            {
              className: "title",
              begin: /\s+[ก-๛a-zA-Z_][ก-๛a-zA-Z0-9_]*/,
              relevance: 0,
              endsWithParent: true,
            },
          ],
        },
        {
          className: "class",
          begin: /\bชั้น\b/,
          end: ":",
          keywords: "ชั้น",
          contains: [
            {
              className: "title",
              begin: /\s+[ก-๛a-zA-Z_][ก-๛a-zA-Z0-9_]*/,
              relevance: 0,
              endsWithParent: true,
            },
          ],
        },
      ],
    };
  }

  // Register the language
  if (typeof window !== "undefined" && window.hljs) {
    window.hljs.registerLanguage("piyathon", piyathonLanguage);
    console.log("Piyathon language registered successfully");

    // Debug: List registered languages
    console.log(
      "Registered languages:",
      Object.keys(window.hljs.listLanguages())
    );
  }

  // Support CommonJS/Node if needed
  if (typeof module !== "undefined" && module.exports) {
    module.exports = piyathonLanguage;
  }
})();
