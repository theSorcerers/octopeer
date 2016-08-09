class Api::HtmlPagesController < ApplicationController
  include TimeHelper
  before_action :set_html_page, only: :show
  before_action only: :create do
    format_time(:html_page)
  end

  def index
    @html_pages = HtmlPage.all

    render json: @html_pages
  end

  def show
    render json: @html_page
  end

  def create
    @html_page = HtmlPage.new(html_page_params)

    if @html_page.save
      render json: @html_page, status: :created
    else
      render json: @html_page.errors, status: :unprocessable_entity
    end
  end

  private

  def set_html_page
    @html_page = HtmlPage.find(params[:id])
  end

  def html_page_params
    params.require(:html_page).permit(:dom, :session_id, :created_at)
  end
end
