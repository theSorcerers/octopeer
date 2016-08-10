class Api::HtmlPagesController < ApplicationController
  include TimeHelper
  include Showable
  include Indexable
  include Createable

  private

  def html_page_params
    params.require(:html_page).permit(:dom, :session_id, :created_at)
  end
end
