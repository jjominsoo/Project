import Link from "next/link"

import MainBox from "../components/MainBox"
import Logo from "../images/Logo.png"
export default function Home() {
  return (
    <div className='flex justify-center items-center h-screen w-full text-main'>
      <MainBox>
        <div className='text-center'>
          <img src={Logo.src} alt='logo' className='m-auto mt-20 w-32' />

          <p className='text-8 mt-20'>
            Get a Recommendation that suit your taste in wine!
          </p>
          <div className='inline-block mt-16 px-10 py-4 text-6 border-b-2 border-main hover:bg-grey-300'>
            <Link href='/question'>
              <a>Get Start 🍷</a>
            </Link>
          </div>
          <br />

          <div className='inline-block mt-4 mb-20 px-10 py-4 text-6 border-b-2 border-main hover:bg-grey-300'>
            <a>Share 🍾</a>
          </div>
        </div>
      </MainBox>
    </div>
  )
}
